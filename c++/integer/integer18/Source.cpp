/*���� ����� �����, ������� 999. ���������
���� �������� ������� ������ � ���� ��������
������ ������� �� �������, ����� �����,
��������������� ������� ����� � ������
����� �����.*/

#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int ans = n % 10000 / 1000;
	cout << ans;

	cout << "\n\n";
	system("pause");
}