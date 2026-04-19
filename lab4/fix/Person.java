/**
 * модель человека
 */
public class Person {
	private final String name;
	private final int height;

	/**
	 * создает человека
	 *
	 * @param name имя
	 * @param height рост
	 */
	public Person(final String name, final int height) {
		this.name = name;
		this.height = height;
	}

	/**
	 * возвращает строку человека
	 *
	 * @return строка с именем и ростом
	 */
	@Override
	public String toString() {
		return name + ", рост: " + height;
	}
}
