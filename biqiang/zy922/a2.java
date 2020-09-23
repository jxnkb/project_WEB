package zy922;

public class a2 {
	//案例:设计一个用户类,类里有私有成员姓名和密码,电话号码.设计这三个私有属性的setter和getter函数
			//其中修改密码需要验证电话号码
	static class usr{
		private String name,phone,password;
		String getname(){
			return name;
		}
		String getphone() {
			return phone;
		}
		String getpassword() {
			return password;
		}
		public void setname(String name) {
			this.name=name;
		}
		public void setpassword(String password,String phone) {
			if(this.phone.equals(phone) ) {
				this.password=password;
			}else {
				System.out.println("输入错误");
			}
		}
		public void setphone(String phone) {
			this.phone=phone;
		}
	}
	
//	案例:在别的文件定义一个类,类中有属性name,age,score,其中age赋值时要判断合法性
//	可以通过构造函数赋值,可以调用打印这些属性的方法
	static class guy{
		String name;
		int age,score;
		guy(String name,int age,int score){
			this.name=name;
			if(age>0 &age<140) {
				this.age=age;
			}else {
				System.out.println("输入不合法");
			}
			this.score=score;
		}
		void getinfo(){
			System.out.println("姓名："+name+" 年龄:"+age+" 分数："+score);
		}
	}
	
	
//	设计一个教室类,属性有房间号,座位数,房间名,类有三个属性的setter和getter属性,要求形参名和属性名一样
	static class room{
		String num,name;
		int seats;
		void setnum(String num){
			this.num=num;
		}
		void setname(String name) {
			this.name=name;
		}
		void setseats(int seats) {
			this.seats=seats;
		}
		String getname() {
			return name;
		}
		String getnum() {
			return num;
		}
		int getseats() {
			return seats;
		}
	}
	
	
//	案例:封装一个狗类,属性有名字,年龄,品种,提供对外接口,通过接口才能访问属性和修改属性,
//	修改年龄属性时需要验证合法性.有构造函数先给这些属性赋值
	static class dog{
		private String name,breed;
		private int age;
		dog(String name,String breed,int age){
			this.name=name;
			this.breed=breed;
			this.age=age;
		}
		public int getAge() {
			return age;
		}
		public String getBreed() {
			return breed;
		}
		public String getName() {
			return name;
		}
		public void setAge(int age) {
			this.age = age;
		}
		public void setBreed(String breed) {
			this.breed = breed;
		}
		public void setName(String name) {
			this.name = name;
		}
	}
	
	//案例:定义一个动物类为父类,里面有动物的名字,年龄,品种.定义三个子类,狗,猫,老虎,然后打印
	//出信息,如:2岁的拉布拉多旺财汪汪汪的叫 
	static class animal {
		String name,breed;
		int age;
		animal(String name,String breed,int age){
			this.name=name;
			this.breed=breed;
			this.age=age;
		}
		void bark(){
			
		}
	}
	
	static class Dog extends animal{
		Dog(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"岁的"+breed+name+"旺旺的叫");
		}
	}
	
	static class Cat extends animal{
		Cat(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"岁的"+breed+name+"喵喵的叫");
		}
	}
	
	static class Tiger extends animal{
		Tiger(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"岁的"+breed+name+"嗷嗷的叫");
		}
	}
	
	static void intro(animal a) {
		a.bark();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		usr u1=new usr();
		u1.setphone("139xxxxx");
		u1.setpassword("123456","sdf");
		System.out.println(u1.getphone());
		
		
		Dog d1=new Dog("大黄", "土狗", 5);
		intro(d1);
				
	}

}
