package maker2��������;

import java.util.Scanner;


public class A03for {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������

		for(int i=0;i<10;i++) {
			System.out.println(i+" ");
		}
		System.out.println("-----");
		
//		����:����һ������,Ȼ���ӡ0���������,����ӡ0���������֮��
		//5
		//0 1 2 3 4 5
		//15
		
		Scanner scan=new Scanner(System.in);
		System.out.println("������һ������:");
		int a=scan.nextInt();
		int b=0;
		for(int i=0;i<=a;i++) {
			b=b+i;
			System.out.println(i);
		}
		System.out.println(b);
		
//		����:n�Ľ׳ˣ����ⲿ��������һ������n
//		5
//		5*24=120
		
		System.out.println("������һ������:");
		int n=scan.nextInt();
		int c=1;
		for(int i=1;i<=a;i++) {
			c=c*i;
			System.out.println(i);
		}
		System.out.println(c);
		
		
		
		
		
		
		
		
		
		
	}

}
