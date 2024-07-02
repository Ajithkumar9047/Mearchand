@echo off
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html %*
