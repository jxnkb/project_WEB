package maker2;

import java.util.Scanner;

public class A08�ַ����� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		int[] arr=new int[5];
		for(int i=0;i<5;i++) {
			arr[i]=i;
		}
		System.out.println(arr);
		
		char[] myarr=new char[5];
		for(int i=0;i<5;i++) {
			myarr[i]='a';
		}
		
		System.out.println(myarr);//1.�ַ��������ֱ�Ӵ�ӡ.
		
		String string="abcde";
		System.out.println(string);
		for(int i=0;i<string.length();i++) {//2.�ַ���.length()���Ի�ȡ�ַ����ĳ���
			System.out.println(string.charAt(i));// 3.string.charAt(i)��ȡ�ַ�����ĳ���ַ�
		}
//		for(char i:string) {//����
//			
//		}
		
//		����:�ӿ���̨�����ַ���,Ȼ����ַ����е��ַ��洢���ַ�������,Ȼ���ӡ����
//		1.str.charAt(i);���Է����ַ����е��ַ�,str���ַ���
//		2.str.length();���Է����ַ����ĳ���,str���ַ���
		Scanner scanner=new Scanner(System.in);
		//�ӿ���̨��ȡ�ַ���
		String str=scanner.next();
		//�����ַ�����
		char[] mych=new char[str.length()];
		//�����鸳ֵ
		for(int i=0;i<mych.length;i++) {//abcd
			mych[i]=str.charAt(i);
		}
		//ע��:�����ڵȺŵ���߱�ʾ�ȴ�������ֵ
		mych[0]='a';
		//�����ڵȺŵ��ұ߱�ʾ������ȡֵ
		char c=mych[0];
		
		
		System.out.println(mych);
		
		
	}

}
