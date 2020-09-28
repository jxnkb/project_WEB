package jt001;

import junit.framework.TestCase;
//junit002 as testing tool
public class junit002 extends TestCase{
	int v1,v2;
	
	protected void setUp(){
		v1=3;
		v2=3;
		System.out.println("setup testcase1");
		
	}
	
	public void testAdd(){
		int r=v1+v2;
		assertTrue(r==6);
	}
	public void tearDown(){
		System.out.println("teardown testcase1");
	}
	
	
}
