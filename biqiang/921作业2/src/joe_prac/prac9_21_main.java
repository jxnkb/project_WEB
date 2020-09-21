package joe_prac;
//公有，私有，默认，保护
public class prac9_21_main {
	static public void pub1() {
		System.out.println("this is a public class");
	}
	static private void pri1() {
		System.out.println("this is a private class ");
	}
	static void def1() {
		System.out.println("this is a default class ");
	}
	static protected void pro1() {
		System.out.println("this is a protected class ");
	}
	public static void main(String[] args) {
		pub1();
		def1();
		pri1();
		pro1();
		//都看得到
	}
}
