package maker2;

public class A04for˫ {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
//		for(int i=0;i<9;i++) {
//			for(int j=1;j<=i;j++) {
//				System.out.print(j+"*"+i+"\t");
//			}
//			System.out.println();
//		}
		
//		����:�žų˷��ھ���
		for(int i=1;i<10;i++) {//i==3
			for(int j=1;j<=i;j++) {//j==3
				int n=i*j;//n==4
				System.out.print(j+"*"+i+"="+n+"\t");
			}
			System.out.println();
		}
	}
	

}
