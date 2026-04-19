/**
 * человек с именем и ростом
 */
public class PersonWithName {
	private final Name fullName;
	private final int height;

	/**
	 * создает человека
	 *
	 * @param fullName полное имя
	 * @param height рост
	 */
	public PersonWithName(final Name fullName, final int height) {
		this.fullName = fullName;
		this.height = height;
	}

	/**
	 * возвращает строку человека
	 *
	 * @return строка с именем и ростом
	 */
	@Override
	public String toString() {
		return fullName + ", рост: " + height;
	}
}