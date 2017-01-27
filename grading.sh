#!/bin/bash
clear

echo == All Source Files ================================= > MY.REPORT
ls *.c *.s *.h >> MY.REPORT
echo >> MY.REPORT
 
echo == COMPILE.ERR ====================================== >> MY.REPORT
cat COMPILE.ERR >> MY.REPORT
echo >> MY.REPORT

echo == SUMMARY.RESULTS ================================== >> MY.REPORT
cat SUMMARY.RESULTS >> MY.REPORT
echo >> MY.REPORT

if grep -q "FAIL" SUMMARY.RESULTS; then
	echo == DETAILED.RESULTS ================================= >> MY.REPORT
	cat DETAILED.RESULT >> MY.REPORT
	echo >> MY.REPORT
fi
echo ===================================================== >> MY.REPORT

vim -p MY.REPORT README* *.c *.h *.s

clear
