import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSortKey;

@DynamoDbBean
public class Notes {

    private String userId;
    private String noteId;
    private String note;
    
    public Notes() {
    }

    

    public Notes(String userId, String noteId) {
        this.userId = userId;
        this.noteId = noteId;
    }



    public Notes(String userId, String noteId, String note) {
        this.userId = userId;
        this.noteId = noteId;
        this.note = note;
    }
    @DynamoDbPartitionKey
    public String getUserId() {
        return userId;
    }
    public void setUserId(String userId) {
        this.userId = userId;
    }

    @DynamoDbSortKey
    public String getNoteId() {
        return noteId;
    }
    public void setNoteId(String noteId) {
        this.noteId = noteId;
    }
    public String getNote() {
        return note;
    }
    public void setNote(String note) {
        this.note = note;
    }

    @Override
    public String toString() {
        return "Notes [UserId=" + this.userId + ", NoteId=" + this.noteId + ", Note=" + this.note + "]";
    }

    

    
    
}
