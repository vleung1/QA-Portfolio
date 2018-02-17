import java.util.UUID;

public class test {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		generateString();
	}

	public static String generateString() {
        String uuid = UUID.randomUUID().toString();
        System.out.println("uuid = " + uuid);
		return uuid;
    }
}
