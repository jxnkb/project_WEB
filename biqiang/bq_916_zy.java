package joe_prac;
	
public class bq_916_zy {
//	2.дһ����������ĺ���
	static int[] createL(int a) {
		int[] L=new int[a];
		for(int i=0;i<a;i++) {
			L[i]=(int)(Math.random()*100);
		}
		
		return L;
	}
	
	
//	3.дһ����ӡ����ĺ���
	static void printL(int[] l) {
		for(int i:l){
			System.out.print(i+" ");
		}
		System.out.println();
	}
	
//	4.дһ��������������ĺ���
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
