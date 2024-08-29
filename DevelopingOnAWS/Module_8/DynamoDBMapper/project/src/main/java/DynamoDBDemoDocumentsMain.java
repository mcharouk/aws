import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import software.amazon.awssdk.enhanced.dynamodb.AttributeConverterProvider;
import software.amazon.awssdk.enhanced.dynamodb.AttributeValueType;
import software.amazon.awssdk.enhanced.dynamodb.TableMetadata;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.document.EnhancedDocument;
import software.amazon.awssdk.enhanced.dynamodb.model.PageIterable;

public class DynamoDBDemoDocumentsMain {
    private static final Logger logger = LoggerFactory.getLogger(DynamoDBDemoDocumentsMain.class);

    

    public static void main(String[] args) {
        NotesGenericService<EnhancedDocument> notesDocumentService = new NotesGenericService<EnhancedDocument>(TableSchema.documentSchemaBuilder()
                    // Specify the primary key attributes.
                    .addIndexPartitionKey(TableMetadata.primaryIndexName(), "userId", AttributeValueType.S)
                    .addIndexSortKey(TableMetadata.primaryIndexName(), "noteId", AttributeValueType.S)
                    // Specify attribute converter providers. Minimally add the default one.
                    .attributeConverterProviders(AttributeConverterProvider.defaultProvider())
                    .build());

        logger.info("Creating Table Notes");
        notesDocumentService.createTable();

        String student_user_id = "student";
        EnhancedDocument[] noteArray = new EnhancedDocument[5];
        noteArray[0] = createEnhancedDocument(student_user_id, "1", "DynamoDB is NoSQL");
        noteArray[1] = createEnhancedDocument(student_user_id, "2", "A DynamoDB table is schemaless");
        noteArray[2] = createEnhancedDocument(student_user_id, "3", "PartiQL is a SQL compatible language for DynamoDB");
        noteArray[3] = createEnhancedDocument(student_user_id, "4", "Maximum size of an item is 400 KB");
        noteArray[4] = createEnhancedDocument(student_user_id, "5", "I love DyDB");

        notesDocumentService.batchWriteItems(noteArray);

        logger.info("Getting a Note by partition Key");
        
        EnhancedDocument enhancedDocument = createEnhancedDocument(student_user_id, "2");
        EnhancedDocument result = notesDocumentService.getItem(enhancedDocument);
        logger.info(result.toJson());
        //result.getListOfUnknownType(attributeName)
        //result.getMapOfUnknownType(attributeName)

        logger.info("Return notes that contains a specific string");
        PageIterable<EnhancedDocument> notes = notesDocumentService.getItemByUserIdLikeString(student_user_id, "language");
        notes.items().forEach(item -> logger.info(item.toJson()));

        // create a new note
        logger.info("Create a new Note");
        EnhancedDocument newEnhancedDocument = createEnhancedDocument("marc.charouk", "1", "Global Secondary indexes can be created after table creation");

        notesDocumentService.putItem(newEnhancedDocument);

        // scan note table
        logger.info("Scan Note table");
        PageIterable<EnhancedDocument> scannedNotes = notesDocumentService.scanTable();
        scannedNotes.items().forEach(item -> logger.info(item.toJson()));

        notesDocumentService.deleteTable();

    }

    private static EnhancedDocument createEnhancedDocument(String user_id, String note_id, String note) {
        // EnhancedDocument.builder().json(null);

        return EnhancedDocument.builder()
                .putString("userId", user_id)
                .putString("noteId", note_id)
                .putString("note", note)
                // .putJson(null, null)
                // .putList(null, null, null)
                // .putMap(null, null, null, null)
                .build();
    }

    private static EnhancedDocument createEnhancedDocument(String user_id, String note_id) {
        // EnhancedDocument.builder().json(null);

        return EnhancedDocument.builder()
                .putString("userId", user_id)
                .putString("noteId", note_id)
                // .putJson(null, null)
                // .putList(null, null, null)
                // .putMap(null, null, null, null)
                .build();
    }

}