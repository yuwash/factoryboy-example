# factoryboy-example
Example django project using factoryboy to populate fake data

## Installation

Run

```
cd "$REPOSITORY_ROOT"
pipenv install
pipenv run python manage.py migrate
```

## Usage

```
$ python manage.py populatefake
$ python manage.py printall
<QuerySet [{'id': 1, 'name': 'Dr. Michel Lindau', 'address': 'Dehmelring 3\n61821 Karlsruhe', 'email': 'sring@gmx.de', 'contract_number': '22816615', 'is_active': True}, {'id': 2, 'name': 'Janine Wagner B.Eng.', 'address': 'Vincent-Anders-Allee 709\n58155 Amberg', 'email': 'wmueller@mangold.de', 'contract_number': '94933622', 'is_active': False}, {'id': 3, 'name': 'Víēlé Ǘmłåūţè', 'address': 'Dirk-Hartmann-Straße 186\n00342 Naila', 'email': 'hiltrudlangern@hotmail.de', 'contract_number': '05838103', 'is_active': True}, {'id': 4, 'name': 'Univ.Prof. Leonore Hofmann MBA.', 'address': '11223344\nPackstation 987\n12345 Kein-Richtiges-Haus', 'email': 'vbenthin@kambs.de', 'contract_number': '61816149', 'is_active': True}, {'id': 5, 'name': 'Ing. Viktoria Henk B.Sc.', 'address': 'Knappestr. 60\n42735 Forchheim', 'email': 'meinrad96@loewer.de', 'contract_number': '90802915', 'is_active': True}, {'id': 6, 'name': 'Dieter Hartung-Scholtz', 'address': 'Gorlitzgasse 58\n36426 Celle', 'email': 'girschnerkenneth@wagner.de', 'contract_number': '45315797', 'is_active': True}, {'id': 7, 'name': 'Alf Riehl', 'address': 'Seipstr. 7/5\n40146 Brand', 'email': 'utrapp@anders.com', 'contract_number': '12390399', 'is_active': False}, {'id': 8, 'name': 'Univ.Prof. Birger Textor B.A.', 'address': 'Sorgatzweg 0/6\n34515 Gardelegen', 'email': 'ellenwulff@wulf.com', 'contract_number': '08520529', 'is_active': True}, {'id': 9, 'name': 'Alfredo Sontag B.Sc.', 'address': 'Annedore-Schleich-Ring 67\n29913 Bitterfeld', 'email': 'dtschentscher@gmail.com', 'contract_number': '16050739', 'is_active': True}]>
<QuerySet [{'id': 1, 'contract_id': 5, 'meter_number': '5858687164', 'size': 15}, {'id': 2, 'contract_id': 8, 'meter_number': '3686375494', 'size': 10}, {'id': 3, 'contract_id': 9, 'meter_number': '6217185010', 'size': 12}]>
<QuerySet [{'id': 1, 'contract_id': 6, 'size': 494.443378000699}]>
<QuerySet [{'id': 1, 'contract_id': 7, 'meter_id': 2, 'begin': datetime.date(2008, 4, 10), 'end': datetime.date(2019, 3, 26)}, {'id': 2, 'contract_id': 2, 'meter_id': 3, 'begin': datetime.date(2007, 10, 1), 'end': datetime.date(2020, 3, 3)}]>
```

You can also call `python manage.py populatefake --huge` to get a lot
more items.
