package Testmaker��������;

import java.util.Scanner;


public class A07Test��Ŀ����� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		int a=10;
		int b=20;
		int c=a>b?a:b;
		System.out.println(c);
		
//		����:�ӿ���̨������������,Ȼ���ӡ��������ֵ
		Scanner scan=new Scanner(System.in);
		System.out.println("�������һ������:");
		int a1=scan.nextInt();
		System.out.println("������ڶ�������:");
		int a2=scan.nextInt();
		System.out.println("���������������:");
		int a3=scan.nextInt();
		
		int b2=a1>a2?(a1>a3?a1:a3):(a2>a3?a2:a3);
		System.out.println(b2);
		
		

	}

}
