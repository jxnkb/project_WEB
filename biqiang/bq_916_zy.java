package joe_prac;
	
public class bq_916_zy {
//	2.写一个创建数组的函数
	static int[] createL(int a) {
		int[] L=new int[a];
		for(int i=0;i<a;i++) {
			L[i]=(int)(Math.random()*100);
		}
		
		return L;
	}
	
	
//	3.写一个打印数组的函数
	static void printL(int[] l) {
		for(int i:l){
			System.out.print(i+" ");
		}
		System.out.println();
	}
	
//	4.写一个可以排序数组的函数
	static int[] buble(int[] l) {
		for(int i=0;i<l.length-1;i++) {
			for(int u=0;u<l.length-1-i;u++) {
				if(l[u]>l[u+1]) {
					int temp=l[u];
					l[u]=l[u+1];
					l[u+1]=temp;
				}
					
			}
		}
		return l;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] l=createL(10);
		printL(l);
		buble(l);
		printL(l);

	}

}
