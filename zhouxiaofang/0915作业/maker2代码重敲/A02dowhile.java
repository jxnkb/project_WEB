package maker2代码重敲;

public class A02dowhile {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		int a=0;
		do {
			System.out.println(a);
			a++;
		}while(a<10); //注意这里有分号
		
//		案例:输出1-100的单数
		int b=1;
		do {
			if(b%2==1) {
				System.out.println(b);
			}
			
			b+=1;
			
		}while(b<=100);
		
//		案例:使用while嵌套循环打印如下图形
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		
		int i=0;
		while(i<5) {
			int j=0;
			while(j<i) {
				System.out.print("*");
				j++;
			}
			
			i++;
			System.out.println();
		}
		
		
		
		
		
		
		

	}

}
