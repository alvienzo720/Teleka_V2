from django.db import models
from django.contrib.auth.models import User 


class SaccoAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Member(models.Model):
	STATUS = (
		('ACTIVE','ACTIVE'),
		('PENDING', 'PENDING'),
		)

	ID_TYPE = (
		('NATIONAL ID', 'NATIONAL ID'),
		('PASSPORT', 'PASSPORT'),
		('DRIVING PERMIT', 'DRIVING PERMIT'),
	    )

	GENDER = (
		('MALE','MALE'),
		('FEMALE', 'FEMALE'),
		)

	DISTRICTS = (
		('Abim','Abim'),
		('Adjumani','Adjumani'),
		('Agago','Agago'),
		('Alebtong','Alebtong'),
		('Amolatar','Amolatar'),
		('Amudat','Amudat'),
		('Amuria','Amuria'),
		('Amuru','Amuru'),
		('Apac','Apac'),
		('Arua','Arua'),
		('Budaka','Budaka'),
		('Bududa','Bududa'),
		('Bugiri','Bugiri'),
		('Bugweri','Bugweri'),
		('Buikwe','Buikwe'),
		('Bukedea','Bukedea'),
		('Bukomansimbi','Bukomansimbi'),
		('Bukwa','Bukwa'),
		('Bulambuli','Bulambuli'),
		('Buliisa','Buliisa'),
		('Bundibugyo','Bundibugyo'),
		('Bunyangabu','Bunyangabu'),
		('Bushenyi','Bushenyi'),
		('Busia','Busia'),
		('Butebo','Butebo'),
		('Buvuma','Buvuma'),
		('Buyende','Buyende'),
		('Dokolo','Dokolo'),
		('Gomba','Gomba'),
		('Gulu','Gulu'),
		('Hoima','Hoima'),
		('Ibanda','Ibanda'),
		('Iganga','Iganga'),
		('Isingiro','Isingiro'),
		('Jinja','Jinja'),
		('Kaabong','Kaabong'),
		('Kabale','Kabale'),
		('Kabarole','Kabarole'),
		('Kaberamaido','Kaberamaido'),
		('Kagadi','Kagadi'),
		('Kakumiro','Kakumiro'),
		('Kalangala','Kalangala'),
		('Kaliro','Kaliro'),
		('Kalungu','Kalungu'),
		('Kampala','Kampala'),
		('Kamuli','Kamuli'),
		('Kamwenge','Kamwenge'),
		('Kanungu','Kanungu'),
		('Kapchorwa','Kapchorwa'),
		('Kapelebyong','Kapelebyong'),
		('Kasanda','Kasanda'),
		('Kasese','Kasese'),
		('Katakwi','Katakwi'),
		('Kayunga','Kayunga'),
		('Kibaale','Kibaale'),
		('Kiboga','Kiboga'),
		('Kibuku','Kibuku'),
		('Kikuube','Kikuube'),
		('Kiruhura','Kiruhura'),
		('Kiryandongo','Kiryandongo'),
		('Kisoro','Kisoro'),
		('Kitgum','Kitgum'),
		('Koboko','Koboko'),
		('Kole','Kole'),
		('Kotido','Kotido'),
		('Kumi','Kumi'),
		('Kwania','Kwania'),
		('Kween','Kween'),
		('Kyankwanzi','Kyankwanzi'),
		('Kyegegwa','Kyegegwa'),
		('Kyenjojo','Kyenjojo'),
		('Kyotera','Kyotera'),
		('Lamwo','Lamwo'),
		('Lira','Lira'),
		('Luuka','Luuka'),
		('Luwero','Luwero'),
		('Lwengo','Lwengo'),
		('Lyantonde','Lyantonde'),
		('Manafwa','Manafwa'),
		('Maracha','Maracha'),
		('Masaka','Masaka'),
		('Masindi','Masindi'),
		('Mayuge','Mayuge'),
		('Mbale','Mbale'),
		('Mbarara','Mbarara'),
		('Mitooma','Mitooma'),
		('Mityana','Mityana'),
		('Moroto','Moroto'),
		('Moyo','Moyo'),
		('Mpigi','Mpigi'),
		('Mubende','Mubende'),
		('Mukono','Mukono'),
		('Nabilatuk','Nabilatuk'),
		('Nakapiripirit','Nakapiripirit'),
		('Nakaseke','Nakaseke'),
		('Nakasongola','Nakasongola'),
		('Namayingo','Namayingo'),
		('Namisindwa','Namisindwa'),
		('Namutumba','Namutumba'),
		('Napak','Napak'),
		('Nebbi','Nebbi'),
		('Ngora','Ngora'),
		('Ntoroko','Ntoroko'),
		('Ntungamo','Ntungamo'),
		('Nwoya','Nwoya'),
		('Omoro','Omoro'),
		('Otuke','Otuke'),
		('Oyam','Oyam'),
		('Pader','Pader'),
		('Pakwach','Pakwach'),
		('Pallisa','Pallisa'),
		('Rakai','Rakai'),
		('Rubanda','Rubanda'),
		('Rubirizi','Rubirizi'),
		('Rukiga','Rukiga'),
		('Rukungiri','Rukungiri'),
		('Sembabule','Sembabule'),
		('Serere','Serere'),
		('Sheema','Sheema'),
		('Sironko','Sironko'),
		('Soroti','Soroti'),
		('Tororo','Tororo'),
		('Wakiso','Wakiso'),
		('Yumbe','Yumbe'),
		('Zombo','Zombo'),
		)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	id_type = models.CharField(max_length=200, null=True, choices=ID_TYPE)
	id_number = models.CharField(max_length=200, null=True)
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	date_of_birth = models.DateField(auto_now_add=False, null=True)
	district = models.CharField(max_length=200, null=True, choices=DISTRICTS)
	county = models.CharField(max_length=200, null=True)
	subcounty = models.CharField(max_length=200, null=True)
	parish = models.CharField(max_length=200, null=True)
	village = models.CharField(max_length=200, null=True)
	account_number = models.CharField(max_length=200, null=True)
	opening_balance = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	next_of_keen_first_name = models.CharField(max_length=200, null=True)
	next_of_keen_last_name = models.CharField(max_length=200, null=True)
	next_of_keen_phone = models.CharField(max_length=200, null=True)
	next_of_keen_relationship = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.firstname + " " + self.lastname

