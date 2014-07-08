#!/bin/bash

#
# CoruGI - Your server status, in a single CGI script.
#
# Install:
# * Copy corugi.cgi to your CGI scripts folder
# * Execute chmod +x corugi.cgi
# * Access via web
#
# Angelito M. Goulart
#
# dec/2012
#
#

echo "Content-type: text/html";
echo "";

/bin/cat << END_HTML

<!doctype html>
<html>
<head>
	
	<title>CoruGI</title>

	<style type="text/css">
		body { font-family: arial, verdana, sans-serif; margin: 0; padding: 0; background-color: #E7E7E7; color: #525050; font-size: 13px;}
		#top { background-color: #4A4747; width: 100%; }
		#top h1 { margin: 0; padding: 10px; color: #6C6868;}
		.general_info { padding-left: 3px; }
		.general_info span { font-weight: bold;}
		.info { padding-left: 3px; height: 150px; overflow: scroll; }
		.title { font-size: 18px; font-weight: bold; margin-top: 10px; padding: 5px; }
		.description { font-style: italic; padding-left: 5px; font-size: 14px; }
		#footer { margin-top: 10px; padding: 5px;}
		#footer a { color: #525050; text-decoration: none;}
		#footer a:hover { color: #525050; text-decoration: underline;}
	</style>

</head>

<body>
	
	<!-- Header -->
	<div id="top">
		<h1>CoruGI</h1>
	</div>

	<div id="content">

		<!-- Description -->
		<p class="description">Stats of your server, in a single CGI script.</p>

		<!-- General Info -->
		<div class="stat">
			<div class="title">General Info</div>
			<div class="general_info">

				<!-- Hostname -->
				<p>Hostname: <span>$(hostname)</span></p>

				<!-- Uptime -->
				<p>Uptime: <span>$(uptime)</span></p>

				<!-- Date -->
				<p>Date: <span>$(date)</span></p>

				<!-- System Info -->
				<p>System Info: <span>$(uname -a)</span></p>

			</div>
		</div>

		<!-- Network Info -->
		<div class="stat">
			<div class="title">Network Info</div>
			<div class="info">
				<pre>$(ifconfig)</pre >
			</div>
		</div>

		<!-- Disk Usage Info -->
		<div class="stat">
			<div class="title">Disk Usage Info</div>
			<div class="info">
				<pre>$(df -h)</pre>
			</div>
		</div>

		<!-- Processes Info -->
		<div class="stat">
			<div class="title">Processes Info</div>
			<div class="info">
				<pre>$(ps -ax)</pre>
			</div>
		</div>

		<!-- Users Info -->
		<div class="stat">
			<div class="title">Users Info</div>
			<div class="info">
				<pre>$(w)</pre>
			</div>
		</div>

		<!-- Input/Output Stats Info -->
		<div class="stat">
			<div class="title">Input/Output Stats Info</div>
			<div class="info">
				<pre>$(iostat)</pre>
			</div>
		</div>

	</div>

	<div id="footer">
		CoruGI - <a href="http://angelitomg.com/">Angelito M. Goulart</a>
	</div>

</body>
</html>

END_HTML
