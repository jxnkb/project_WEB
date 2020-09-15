package maker2代码重敲;

public class A04双for循环 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
//		for(int i=0;i<9;i++) {
//			
//			for(int j=1;j<i;j++) {
//				System.out.println(j+"*"+i+"\t");
//			}
//			System.out.println();
//		}
		
//		案例:九九乘法口诀表	
		for(int i=1;i<10;i++) {
			
			for(int j=1;j<=i;j++) {
				int n=i*j;
				System.out.print(j+"*"+i+"="+n+"\t");
			}
			System.out.println();
		}
		
		

	}

}
