<!DOCTYPE html>
<html>
<head>
	<title>app</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>

<body>

    <h2>byrting upplysinga</h2>
    <img src="/static/ao.png">
    <img src="/static/n1.png">
    <img src="/static/daelan.png">
    <img src="/static/skeljungur.png">
    <img src="/static/costco.png">
    <img src="/static/olis.png">
    <img src="/static/ob.png">
    <img src="/static/orkan.png">
    <img src="/static/orkanx.png">
    
    <%
listi = list()
for i in data['results']:
    listi.append(i['company'])
end
listi = set(listi)
listi = sorted(listi)
%>
%print(listi)
<table>
%for i in listi:
    <tr><td><a href="/company/{{i}}">{{i}}</a></td></tr>
%end
</table>

</body>
</html>
