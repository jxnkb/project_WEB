package joe_prac;

import java.awt.List;
import java.util.PrimitiveIterator;
import java.util.Scanner;

import javax.xml.ws.AsyncHandler;

public class bq9_14zy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		

//		��.������װeclipse
//		��.д��main��������Ҫ��
//	�������η�:public����������:void��������:main��������:�������ڵ��������ݣ�
//		��.��д��int,float,double,char,long�ֱ�ռ�ڴ�Ĵ�С
//			int 4�ֽڣ�float4�ֽڣ�double8�ֽڣ�char2�ֽڣ�long8�ֽ�
//		��.ǿ������ת����ôת��
//		�������� ����=���������ͣ�����
//		��.�����
		
//		System.out.println("���һ�����֣�");
//		int a=scanner.nextInt();
//		int b=100;
//		if(a<b) {
//			System.out.println("С��");
//		}else if (a>b) {
//			System.out.println("����");
//		}else {
//			System.out.println("��ϲ��¶���");
//		}
		
//		һ.����Ĵ�����дһ��
//		System.out.println("hi");
//		int a1=1,b1=2,c1=3;
//		System.out.printf("a1=%d,b2=%d,c1=%d",a1,b1,c1);
		
		byte a2=100;
		int b2=a2;
		System.out.println(a2);
		
		int c2=1111;
		byte d2=(byte)c2;
		System.out.println(d2);
		
		char e2=']';
		String e3="]";
		System.out.println(e3+1);
		System.out.println(e2+1);
//		Scanner ax =new Scanner(System.in);
//		int ax1=ax.nextInt();
		
//		����:�ӿ���̨������������,Ȼ���ӡ��������ֵ
//		System.out.println("��������������");
//		int a4=scanner.nextInt();
//		int b4=scanner.nextInt();
//		int c4=scanner.nextInt();
//		if(a4>b4 &a4>c4) {
//			System.out.println(a4);
//		}else if(b4>a4&b4>c4) {
//			System.out.println(b4);
//		}else {
//			System.out.println(c4);
//		}
		
//		if (a4>b4) {
//			if(a4>c4) {
//				System.out.println(a4);
//			}else {
//				System.out.println(c4);
//			}
//		}else {//a4<=b4
//			if(b4>c4) {
//				System.out.println(b4);
//			}else {
//				System.out.println(c4);
//			}
//		}
		
		
//		����:�ӿ���̨����һ������,�ñ���a����,�������������10,�ʹ�ӡ"��������ݴ���10"
//		int a5=scanner.nextInt();
//		if(a5>10) {
//			System.out.println("�������ֵ����10");
//		}
		
////		����:�����·ݣ������Ӧ�ļ��ڣ�
//		System.out.println("�����·ݣ�");
//		int a6=scanner.nextInt();
//		if(a6>=1&a6<=3) {
//			System.out.println("����");
//		}else if(a6>=4&a6<=6) {
//			System.out.println("����");
//		}else if (a6>=7&a6<=9) {
//			System.out.println("����");
//		}else if (a6>=10&a6<=12) {
//			System.out.println("����");
//		}else {
//			System.out.println("�������");
//		}
		

//		����:�����������ͱ���,Ȼ��ӿ���̨��ȡһ���ַ�,�����+��ô���������������,����ʲô���žͶ�Ӧ����ʲô
//		//�ӿ���̨��ȡһ���ַ�
		int b7=12,c7=123;
		System.out.println("���������");
		char a7=scanner.next().charAt(0);
		switch (a7) {
		case '+':
			System.out.println(b7+c7);
			break;
		case '-':
			System.out.println(b7-c7);
			break;
		case '*':
			System.out.println(b7*c7);
			break;
		case '/':
			System.out.println(b7/c7);
			break;

		default:
			System.out.println("�������");
			break;
		}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
