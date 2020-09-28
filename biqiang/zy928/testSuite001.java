package jt001;

import junit.framework.TestResult;
import junit.framework.TestSuite;

//as a testing suite
public class testSuite001 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TestSuite ts=new TestSuite(junit003.class,junit004.class);
		
		TestResult tr=new TestResult();
		
		ts.run(tr);
		
		System.out.println("测试套件运行数量:"+tr.runCount());
	}

}
