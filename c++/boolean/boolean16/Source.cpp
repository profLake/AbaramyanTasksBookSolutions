/*���� ����� ������������� �����. ���������
���������� ������������: "������ �����
�������� ������ ����������".*/

#include "../boolean.h"

int main()
{
	int n = get_n("n");
	
	print_bool(!(n % 2) && digit(n) == 2);

	exit();
}