/**
 * структура полного имени
 */
public class Name {
	private final String lastName;
	private final String firstName;
	private final String middleName;

	/**
	 * создает имя
	 *
	 * @param lastName фамилия
	 * @param firstName имя
	 * @param middleName отчество
	 */
	public Name(
		final String lastName,
		final String firstName,
		final String middleName
	) {
		this.lastName = lastName;
		this.firstName = firstName;
		this.middleName = middleName;
	}

	/**
	 * возвращает имя одной строкой
	 *
	 * @return строка с именем
	 */
	@Override
	public String toString() {
		final StringBuilder sb = new StringBuilder();

		if (lastName != null && !lastName.isEmpty()) {
			sb.append(lastName);
		}

		if (firstName != null && !firstName.isEmpty()) {
			if (!sb.isEmpty()) {
				sb.append(" ");
			}

			sb.append(firstName);
		}

		if (middleName != null && !middleName.isEmpty()) {
			if (!sb.isEmpty()) {
				sb.append(" ");
			}

			sb.append(middleName);
		}

		return sb.toString();
	}
}
