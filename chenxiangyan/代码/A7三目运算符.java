package test3;
import java.util.Scanner;
public class A7��Ŀ����� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
    int a=10;
    int b=20;
    int c=a>b?a:b;
    System.out.println(c);
    
//	����:�ӿ���̨������������,Ȼ���ӡ��������ֵ
    Scanner scanner=new Scanner(System.in);
    System.out.println("�������һ������");
    int a1=scanner.nextInt();
    System.out.println("������ڶ�������");
    int a2=scanner.nextInt();
    System.out.println("���������������");
    int a3=scanner.nextInt();
    int b2=a1>a2?(a1>a3?a1:a3):(a2>a3?a2:a3);
    System.out.println(b2);
	}

}
