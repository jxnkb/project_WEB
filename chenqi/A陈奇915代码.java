package twoday;
import java.util.function.IntConsumer;
public class A����915���� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
//		����:����һ������������,Ȼ��������,Ȼ�������ӡ
		int[] myarr=new int[5];
		for(int i=0;i<5;i++) {
			myarr[i]=(int)(Math.random()*100);
		}
		for(int i:myarr) {
			System.out.print(i+" ");
		}
		for(int i=0;i<myarr.length/2;i++) {
			int tmp=myarr[i];
			myarr[i]=myarr[myarr.length-1-i];
			myarr[myarr.length-1-i]=tmp;
		}
		System.out.println();
		for(int i:myarr) {
			System.out.print(i+" ");
		
		}
	}

}
