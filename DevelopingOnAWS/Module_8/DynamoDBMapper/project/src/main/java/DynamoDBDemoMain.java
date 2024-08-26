import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.PageIterable;

public class DynamoDBDemoMain {
    private static final Logger logger = LoggerFactory.getLogger(DynamoDBDemoMain.class);

    public static void main(String[] args) {
        NotesGenericService<Notes> notesService = new NotesGenericService<Notes>("Notes", TableSchema.fromBean(Notes.class));

        logger.info("Creating Table Notes");
        notesService.createTable();

        String student_user_id = "student";
        Notes[] noteArray = new Notes[5];
        
        noteArray[0] = new Notes(student_user_id, "1", "DynamoDB is NoSQL");
        noteArray[1] = new Notes(student_user_id, "2", "A DynamoDB table is schemaless");
        noteArray[2] = new Notes(student_user_id, "3", "PartiQL is a SQL compatible language for DynamoDB");
        noteArray[3] = new Notes(student_user_id, "4", "Maximum size of an item is 400 KB");
        noteArray[4] = new Notes(student_user_id, "5", "I love DyDB");
        notesService.batchWriteItems(noteArray);

        logger.info("Getting a Note by partition Key");
        Notes note = new Notes(student_user_id, "2");
        note = notesService.getItemByPartitionKey(note);
        logger.info(note.toString());

        logger.info("Return notes that contains a specific string");
        PageIterable<Notes> notes = notesService.getItemByUserIdLikeString(student_user_id, "language");
        notes.items().forEach(item -> logger.info(item.toString()));

        // create a new note
        logger.info("Create a new Note");
        Notes newNote = new Notes("marc.charouk", "1", "Global Secondary indexes can be created after table creation");
        notesService.putItem(newNote);

        // scan note table
        logger.info("Scan Note table");
        PageIterable<Notes> scannedNotes = notesService.scanTable();
        scannedNotes.items().forEach(item -> logger.info(item.toString()));

        notesService.deleteTable();

    }

}