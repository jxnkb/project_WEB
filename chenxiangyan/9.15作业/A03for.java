package maker2;

import java.util.Scanner;

public class A03for {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		for(int i=0;i<10;i++) {
			System.out.print(i+" ");
		}
		System.out.println("-------------");
//		����:����һ������,Ȼ���ӡ0���������,����ӡ0���������֮��
		//5
		//0 1 2 3 4 5
		//15
		Scanner scanner=new Scanner(System.in);
		System.out.println("������һ ����");
		int a=scanner.nextInt();
		int s=0;
		for(int i=0;i<=a;i++) {
			System.out.println(i);
			s+=i;
		}
		System.out.println(s);
		System.out.println("-------");
//		����:n�Ľ׳ˣ����ⲿ��������һ������n
//		5
//		5*24=120
		int a1=scanner.nextInt();
		int s1=1;
		for(int i=1;i<=a1;i++) {
			s1*=i;
		}
		System.out.println(s1);

	}


}
