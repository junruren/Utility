#!/bin/bash
./runTests

clear

echo == All Source Files ================================= > MY.REPORT
ls *.c *.s *.h >> MY.REPORT
echo >> MY.REPORT
 
echo == COMPILE.ERR ====================================== >> MY.REPORT
cat COMPILE.ERR >> MY.REPORT
echo >> MY.REPORT

echo == MILESTONE.MAIL =================================== >> MY.REPORT
cat MILESTONE.MAIL >> MY.REPORT
echo >> MY.REPORT

echo == SUMMARY.RESULTS ================================== >> MY.REPORT
cat SUMMARY.RESULTS >> MY.REPORT
echo >> MY.REPORT

if grep -q "FAIL" SUMMARY.RESULTS; then
	echo == DETAILED.RESULTS ================================= >> MY.REPORT
	cat DETAILED.RESULT >> MY.REPORT
	echo >> MY.REPORT
fi
echo == bset, bclr, btog ================================= >> MY.REPORT

if grep -q "bset" *.s; then
	echo !! bset used >> MY.REPORT
fi

if grep -q "bclr" *.s; then
	echo !! bclr used >> MY.REPORT
fi

if grep -q "btog" *.s; then
	echo !! btog used >> MY.REPORT
fi

echo ===================================================== >> MY.REPORT

vim -p MY.REPORT README* 
vim -p *.h
vim -p *.c
vim -p *.s


clear
./99_ulimit_test.sh.self
echo *** Ref ***
cat RESULT.ulimit_test.refsol
echo --- Stu ---
cat RESULT.ulimit_test.student
echo === END ===
