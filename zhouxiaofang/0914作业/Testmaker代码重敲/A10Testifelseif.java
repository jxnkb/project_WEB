package Testmaker��������;

import java.util.Scanner;

public class A10Testifelseif {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		int a=10;
		int b=20;
		if(a>b) {
			System.out.println("a>b");
			
		}
		
	//	if(a++>b++);
	//	System.out.println("a="+a);
	//	System.out.println("b="+b);
		
		
		if(a>b) {
			System.out.println("a>b");
		}else if(a<b) {
			System.out.println("a>b");
		}else {
			System.out.println("a==b");
		}
		
		
//		����:�����·ݣ������Ӧ�ļ��ڣ�
//		1~3--����
//		4~6--�ļ�
//		7~9--�＾
//		10~12--����
		
		Scanner scan=new Scanner(System.in);
		System.out.println("������һ���·�:");
		int a1=scan.nextInt();
		
		if(a1>=1 && a1<=3) {
			System.out.println("����");
		}else if(a1>=4 && a1<=6) {
			System.out.println("�ļ�");
		}else if(a1>=7 && a1<=9) {
			System.out.println("�＾");
		}else if(a1>=10 && a1<=12) {
			System.out.println("����");
		}else {
			System.out.println("�������");
		}
		

	}

}
