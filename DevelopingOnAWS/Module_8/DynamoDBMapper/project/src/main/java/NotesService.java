import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import software.amazon.awssdk.core.internal.waiters.ResponseOrException;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.Expression;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.BatchWriteItemEnhancedRequest;
import software.amazon.awssdk.enhanced.dynamodb.model.PageIterable;
import software.amazon.awssdk.enhanced.dynamodb.model.QueryConditional;
import software.amazon.awssdk.enhanced.dynamodb.model.QueryEnhancedRequest;
import software.amazon.awssdk.enhanced.dynamodb.model.WriteBatch;
import software.amazon.awssdk.enhanced.dynamodb.model.WriteBatch.Builder;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableResponse;
import software.amazon.awssdk.services.dynamodb.waiters.DynamoDbWaiter;

public class NotesService {

    private static final Logger logger = LoggerFactory.getLogger(NotesService.class);

    private static NotesService INSTANCE;

    private NotesService() {
    }

    public static NotesService getInstance() {
        if (INSTANCE == null) {
            INSTANCE = new NotesService();
        }
        return INSTANCE;
    }

    private DynamoDbClient client = DynamoDbClient.builder().region(Region.EU_WEST_3).build();
    private DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.create();
    private DynamoDbTable<Notes> notesTable = enhancedClient.table("Notes", TableSchema.fromBean(Notes.class));

    public void createTable() {
        notesTable.createTable();

        try (DynamoDbWaiter waiter = DynamoDbWaiter.builder().client(client).build()) { // DynamoDbWaiter is
                                                                                        // Autocloseable
            ResponseOrException<DescribeTableResponse> response = waiter
                    .waitUntilTableExists(builder -> builder.tableName("Notes").build())
                    .matched();
            DescribeTableResponse tableDescription = response.response().orElseThrow(
                    () -> new RuntimeException("Notes table was not created."));
            // The actual error can be inspected in response.exception()
            logger.info("Notes table was created.");
        }
    }

    public void batchWriteItems(Notes[] notes) {
        // Build WriteBatch Item (one per table)
        Builder<Notes> writeBatchBuilder = WriteBatch.builder(Notes.class)
                .mappedTableResource(notesTable);
        for (Notes note : notes) {
            writeBatchBuilder.addPutItem(note);
        }
        WriteBatch writeBatch = writeBatchBuilder.build();

        // build enhanced request (could contain multiple writebatch if multiple table
        // are provided)
        BatchWriteItemEnhancedRequest batchWriteItemEnhancedRequest = BatchWriteItemEnhancedRequest.builder()
                .addWriteBatch(writeBatch).build();
        enhancedClient.batchWriteItem(batchWriteItemEnhancedRequest);

        logger.info("Batch write successful");
    }

    public Notes getItemByPartitionKey(Notes notes) {
        return notesTable.getItem(notes);

    }

    public PageIterable<Notes> getItemByUserIdLikeString(String userId, String likeString) {
        QueryConditional keyEqual = QueryConditional.keyEqualTo(b -> b.partitionValue(userId));

        final Expression filterLikeString = Expression.builder().expression("contains(#column, :containString)")
                .expressionNames(Map.of("#column", "note"))
                .expressionValues(Map.of(":containString", AttributeValue.fromS(likeString))).build();

        QueryEnhancedRequest tableQuery = QueryEnhancedRequest.builder()
                .queryConditional(keyEqual)
                .filterExpression(filterLikeString)
                .build();

        return notesTable.query(tableQuery);
    }

    public PageIterable<Notes> scanTable() {
        return notesTable.scan();
    }

    public void putItem(Notes note) {
        notesTable.putItem(note);
        logger.info("PutItem successful");
    }

    public void deleteTable() {
        notesTable.deleteTable();

        try (DynamoDbWaiter waiter = DynamoDbWaiter.builder().client(client).build()) { // DynamoDbWaiter is
            // Autocloseable
            waiter
                    .waitUntilTableNotExists(builder -> builder.tableName("Notes").build())
                    .matched();            
            // The actual error can be inspected in response.exception()
            logger.info("Notes table was deleted.");
        }

    }

}