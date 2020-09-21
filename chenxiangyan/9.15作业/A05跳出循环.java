package maker2;

public class A05跳出循环 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		int a=1;
		//当a==6时,跳出循环,break;
		while(true) {
			a+=1;
			if(a==6) {
				break;
			}
			System.out.println(a);
			
		}
		
		for(int i=0;i<10;i++) {
			if(i==6) {
				break;
			}
			System.out.println(i);
		}
		System.out.println("------------");
		int b=0;
		while(true) {	
			while(true) {
				b+=1;
				if(b==6) {
					break;//一个break只能跳出一个循环
				}		
			}
			System.out.println(b);
			break;
			
		}
		System.out.println("---------");
		//打印0-9的数字,不要打印出5来
		for(int i=0;i<10;i++) {
			if(i==5) {
				continue;
			}
			System.out.println(i);
		}
		System.out.println("----------");
		aa:for(int i=1;i<3;i++) {
			for(int j=1;j<3;j++) {
				if(j%2==0) {
					break aa;//这种方式,一个break跳出2个循环
				}
				System.out.println("i="+i);
				System.out.println("j="+j);
				
			}
		}
		
		System.out.println("双循环结束");
		aa:for(int i=1;i<3;i++) {
			for(int j=1;j<3;j++) {
				if(j%2==0) {
					continue aa;//这种方式,一个break跳出2个循环
				}
				System.out.println("i="+i);
				System.out.println("j="+j);
				
			}
		}
	}

}
