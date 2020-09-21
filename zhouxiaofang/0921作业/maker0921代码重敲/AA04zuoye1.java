package maker0921代码重敲;

public class AA04zuoye1 {

	

//	6.	编写一个游戏人物类,单独文件编写,游戏人物的属性有姓名,年龄,门派,性别,
//	写出这些属性的getter和setter方法,年龄和性别要检验才能赋值

		
		private String name;
		private int age;
		private String menpai;
		private String sex;
		
		//设置姓名
		void setName(String name1) {
			name=name1;
		}
		
		//获取姓名
		String getName() {
			return name;
		}
		
		
		//设置年龄
		void setAge(int age1) {
			if(age1>0 && age1<140) {
				age=age1;
			}else {
				System.out.println("输入的年龄不合法");
			}
			
		}			
		//获取年龄
		int getAge() {
			return age;
		}
		
		//设置门派
		void setMenpai(String menpai1) {
			menpai=menpai1;
		}
		
		//获取门派
		String getMenpai() {
			return menpai;
		}
		
		//设置性别
		void setSex(String sex1) {
			if(sex1=="男" || sex1=="女" ) {
				sex=sex1;
			}else {
				System.out.println("输入的性别不合法");
			}
					
		}			
		//获取性别
		String getSex() {
			return sex;
		}
		
	
		
}	


