curl \
	-H "Content-Type: application/json" \
	-X PUT \
	"http://localhost:8080/o/headless-delivery/v1.0/document-folders/${1}" \
	-d "{\"name\": \"Goo\"}" \
	-u "test@liferay.com:test"