package maker;

public class BB02保护 {
	
	protected void test03() {
		System.out.println("我是别的包中的test03函数");
	}
	
	protected int myb=200;
	
    public void test003() {
    	test03();
    }
	
    public int getMyb() {
    	return myb;
    }
	
}
