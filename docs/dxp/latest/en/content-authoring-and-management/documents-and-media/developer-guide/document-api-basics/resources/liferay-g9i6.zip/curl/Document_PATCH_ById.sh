curl \
	-F "document={\"description\": \"Bar\"}" \
	-F "file=@Document_POST_ToSite.sh" \
	-H "Content-Type: multipart/form-data; boundary=ARBITRARY" \
	-X PATCH \
	"http://localhost:8080/o/headless-delivery/v1.0/documents/${1}" \
	-u "test@liferay.com:test"