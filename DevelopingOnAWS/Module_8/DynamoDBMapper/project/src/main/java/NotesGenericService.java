import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.common.reflect.TypeToken;

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

public class NotesGenericService<T> {

    private static final Logger logger = LoggerFactory.getLogger(NotesGenericService.class);

    private final DynamoDbClient client = DynamoDbClient.builder().region(Region.EU_WEST_3).build();
    private final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.create();
    private final DynamoDbTable<T> ddbTable;
    private final Class<T> classType;
    private final String tableName = "Notes";
    
    public NotesGenericService(TableSchema<T> tableSchema){
        TypeToken<T> typeToken = new TypeToken<T>(getClass()) {};  
        this.classType = (Class<T>) typeToken.getRawType();

        this.ddbTable = enhancedClient.table(tableName, tableSchema);;
     }

    

    public void createTable() {
        ddbTable.createTable();

        try (DynamoDbWaiter waiter = DynamoDbWaiter.builder().client(client).build()) { // DynamoDbWaiter is
                                                                                        // Autocloseable
            ResponseOrException<DescribeTableResponse> response = waiter
                    .waitUntilTableExists(builder -> builder.tableName(ddbTable.tableName()).build())
                    .matched();
            DescribeTableResponse tableDescription = response.response().orElseThrow(
                    () -> new RuntimeException("Notes table was not created."));
            // The actual error can be inspected in response.exception()
            logger.info("Notes table was created.");
        }
    }

    public void batchWriteItems(T[] notes) {
        // Build WriteBatch Item (one per table)
        Builder<T> writeBatchBuilder = WriteBatch.builder(classType)
                .mappedTableResource(ddbTable);
        for (T note : notes) {
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

    public T getItem(T notes) {
        return ddbTable.getItem(notes);

    }

    public PageIterable<T> getItemByUserIdLikeString(String userId, String likeString) {
        QueryConditional keyEqual = QueryConditional.keyEqualTo(b -> b.partitionValue(userId));

        final Expression filterLikeString = Expression.builder().expression("contains(#column, :containString)")
                .expressionNames(Map.of("#column", "note"))
                .expressionValues(Map.of(":containString", AttributeValue.fromS(likeString))).build();

        QueryEnhancedRequest tableQuery = QueryEnhancedRequest.builder()
                .queryConditional(keyEqual)
                .filterExpression(filterLikeString)                
                .build();

        return ddbTable.query(tableQuery);
    }

    public PageIterable<T> scanTable() {
        return ddbTable.scan();
    }

    public void putItem(T note) {
        ddbTable.putItem(note);
        logger.info("PutItem successful");
    }

    public void deleteTable() {
        ddbTable.deleteTable();

        try (DynamoDbWaiter waiter = DynamoDbWaiter.builder().client(client).build()) { // DynamoDbWaiter is
            // Autocloseable
            waiter
                    .waitUntilTableNotExists(builder -> builder.tableName(ddbTable.tableName()).build())
                    .matched();
            // The actual error can be inspected in response.exception()
            logger.info("Notes table was deleted.");
        }

    }

}
