package maker2��������;

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
		//1.�ַ��������ֱ�Ӵ�ӡ
		System.out.println(myarr);
		
		String str="abcde";
		System.out.println(str);
		for(int i=0;i<str.length();i++) {//2.�ַ���.length()���Ի�ȡ�ַ����ĳ���
			System.out.println(str.charAt(i));// 3.string.charAt(i)��ȡ�ַ�����ĳ���ַ�
		}
		
	//	for(char i:str) { //����
			
	//	}
		
//		����:�ӿ���̨�����ַ���,Ȼ����ַ����е��ַ��洢���ַ�������,Ȼ���ӡ����
//		1.str.charAt(i);���Է����ַ����е��ַ�,str���ַ���
//		2.str.length();���Է����ַ����ĳ���,str���ַ���
		
		Scanner str1=new Scanner(System.in);
		//�ӿ���̨��ȡ�ַ���
		String mystr=str1.next();
		//�����ַ�����
		char[] mych=new char[mystr.length()];
		//�����鸳ֵ
		for(int i=0;i<mych.length;i++) {
			mych[i]=mystr.charAt(i);
		}
		//ע��:�����ڵȺŵ���߱�ʾ�ȴ�������ֵ
		mych[0]='a';
		//�����ڵȺŵ��ұ߱�ʾ������ȡֵ
		char c=mych[0];
		
		System.out.println(mych);
		
	
		
		
		
	}

}
