public class Person {
    private final String name;
    private final int height;

    public Person(String name, int height) {
        this.name = name;
        this.height = height;
    }

    public String toString() {
        return name + ", рост: " + height;
    }
}
