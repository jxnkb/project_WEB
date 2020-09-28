package jt001;

import org.junit.Test;

import junit.framework.TestCase;
//as a TestCast for a TestSuite;
public class junit003 extends TestCase{
	@Test
	public void test01(){
		System.out.println("running test01");
		int num=5;
		String tmp="hi";
		String str="hello";
		
		assertEquals("hi",tmp);
		assertFalse(num>8);
		assertNotNull(tmp);
		
		System.out.println("test01 finished");
	}
	
}
