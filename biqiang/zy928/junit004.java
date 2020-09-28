package jt001;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import junit.framework.TestCase;

//as a TestCast for a TestSuite;
public class junit004 extends TestCase{
	int v1,v2;
	
	@Before
	public void setUp(){
		v1=1;
		v2=3;
		System.out.println("this is setup function");
	}
	
	@Test
	public void test02(){
		System.out.println("running test02");
		System.out.println("test02被调用的次数："+this.countTestCases());
		
		String name=this.getName();
		
		System.out.println("name="+name);
		
		this.setName("test002");
		String name2=this.getName();
		System.out.println("name2="+name2);
		
		System.out.println("test01 done");
	}
	
	@After
	public void tearDown(){
		System.out.println("this is teardown function");
	}
	
	
	
}
