import com.liferay.headless.delivery.client.resource.v1_0.DocumentResource;

public class Document_DELETE_ById {

	/**
	 * java -classpath .:* -DdocumentId=1234 Document_DELETE_ById
	 */
	public static void main(String[] args) throws Exception {
		DocumentResource.Builder builder = DocumentResource.builder();

		DocumentResource documentResource = builder.authentication(
			"test@liferay.com", "test"
		).build();

		documentResource.deleteDocument(
			Long.valueOf(System.getProperty("documentId")));
	}

}