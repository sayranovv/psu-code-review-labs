public class PersonWithName {
    private final Name fullName;
    private final int height;

    public PersonWithName(Name fullName, int height) {
        this.fullName = fullName;
        this.height = height;
    }

    @Override
    public String toString() {
        return fullName + ", рост: " + height;
    }
}