<%@ include file="init.jsp" %>

<portlet:actionURL name="oauthAuthorize" var="oauthAuthorize" />

<% String token = renderRequest.getAttribute("token");

	if (token = "none") {
%>
<p>
<a href="http://localhost:8080/o/oauth2/authorize?response_type=code&client_id=id-e1bbc8d0-ac24-4560-9f41-3287876d1cd3">Click Here to Authorize</a>
</p>

<%
	} else {
%>
<!-- do other stuff -->

<%
	}
%>
