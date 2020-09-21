package joe_prac;

public class bq921zy {
//	今天的代码敲一遍
//	1.类的成员权限全有什么
//	public, private, default, protected
//	2.保护权限和默认权限的区别是什么
//	保护权限可以被不同包的子类读取，默认权限不可以被不同包的子类读取；
//	3.类内可以访问私有权限的成员吗？
//	可以
//	4.当我们要访问类中的私有成员时，我们一般会怎么做？
//		1、创建一个公有权限，用这个公有权限调用私有成员；2、创建一个子类，用子类的公有权限调用这个私有权限；
//	5.一般把什么成员定义为私有的
//	数据
//	6.编写一个游戏人物类,单独文件编写,游戏人物的属性有姓名,年龄,门派,性别,
//	写出这些属性的getter和setter方法,年龄和性别要检验才能赋值
	String name,clan,gender;
	int age;
	String getName(){
		return name;
	}
	String getClan(){
		return clan;
	}
	String getGender(){
		return gender;
	}
	int getAge() {
		return age;
	}
	void setName(String Name) {
		name=Name;
	}
	void setAge(int Age) {
		if(Age >= 0 & Age <=140 ) {
			age=Age;
		}
	}
	void setClan(String Clan) {
		clan=Clan;
	}
	void setGender(String Gender) {
		if(Gender=="男"|Gender=="女") {
			gender=Gender;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		bq921zy hero1= new bq921zy();
		hero1.setAge(18);
		hero1.setClan("武当");
		hero1.setGender("男");
		hero1.setName("王重阳");
		System.out.println(hero1.getAge());
		System.out.println(hero1.getName());
		System.out.println(hero1.getClan());
		System.out.println(hero1.getGender());
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
