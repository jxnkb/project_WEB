package twoday;
import java.util.function.IntConsumer;
public class A陈奇915代码 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
//		案例:定义一个整型数数组,然后赋予数据,然后逆序打印
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
