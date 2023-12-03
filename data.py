import enum


class ContentType(int, enum.Enum):
    text = 0
    video = 1


class NodeStatus(int, enum.Enum):
    to_learn = 0  # Пользователь ещё не ознакомился с вершиной (серый цвет)
    learned = 1  # Пользователь знает вершину (зелёный цвет)
    to_repeat = 2  # Пользователю нужно повторить эту вершину (жёлтый цвет)
    finish = 3
    basic = 4



class TestStatus(int, enum.Enum):
    passed = 0
    not_passed = 1


class UpdateStatus(int, enum.Enum):
    no_updates = 0
    update_received = 1


class ContentUnit:
    def __init__(self, id: str, title: str, contentType: ContentType, summary: str, duration: str, url: str,
                 done: bool = False, liked: bool = False):
        self.id = id
        self.title = title
        self.contentType = contentType  # 0 - text, 1 - video
        self.summary = summary  # random
        self.duration = duration  # random('1 час 30 минут, 45 минут, 10 минут, ...)
        self.url = url
        self.done = done  # false
        self.liked = liked  # false

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "contentType": self.contentType,
            "summary": self.summary,
            "duration": self.duration,
            "url": self.url,
            "done": self.done,
            "liked": self.liked
        }


class Update:
    def __init__(self, status: UpdateStatus, title: str, text: str, url: str, timestamp: str):
        self.status = status
        self.title = title
        self.text = text
        self.url = url
        self.timestamp = timestamp

    def serialize(self):
        if self.status == UpdateStatus.update_received:
            return {
                "status": self.status,
                "title": self.title,
                "text": self.text,
                "url": self.url,
                "timestamp": self.timestamp
            }
        else:
            return {
                "status": self.status
            }



math_graph = {
        "nodes": [
            ["node1", "Целые числа", NodeStatus.learned],
            ["node2", "Натуральные числа", NodeStatus.to_learn],
            ["node3", "Действительные числа", NodeStatus.to_learn],
            ["node4", "Степень с целым показателем", NodeStatus.to_learn],
            ["node5", "Дроби, проценты, рациональные числа", NodeStatus.to_learn],
            ["node6", "Степень с рациональным показателем и ее свойства", NodeStatus.to_learn],
            ["node7", "Свойства степени с действительным показателем", NodeStatus.to_learn],
            ["node8", "Степень с натуральным показателем", NodeStatus.to_learn],
            ["node9", "Свойства степени с действительным показателем", NodeStatus.to_learn],
            ["node11", "Корень степени и его свойства", NodeStatus.to_learn],
            ["node12", "Показательная функция, ее график", NodeStatus.to_learn],
             ["node13", "Логарифмическая функция, ее график", NodeStatus.to_learn],
             ["node14", "Логарифм числа", NodeStatus.to_learn],
             ["node15", "Логарифм произведения, частного, степени", NodeStatus.to_learn],
             ["node16", "Десятичный и натуральный логарифмы, число е", NodeStatus.to_learn],
             ["node17", "Преобразования выражений", NodeStatus.to_learn],
             ["node18", "Преобразования тригонометрических выражений", NodeStatus.to_learn],
             ["node19", "Преобразования выражений, включающих арифметические операции", NodeStatus.to_learn],
             ["node20", "Преобразования выражений, включающих корни натуральной степени", NodeStatus.to_learn],
             ["node21", "Преобразования выражений, включающих операцию возведения в степень", NodeStatus.to_learn],
             ["node22", "Преобразование выражений, включающих операцию логарифмирования", NodeStatus.to_learn],
             ["node23", "Модуль (абсолютная величина) числа", NodeStatus.to_learn],
             ["node24", "Свойства модуля", NodeStatus.to_learn],
             ["node25", "Функция, область определения функции", NodeStatus.to_learn],
             ["node26", "Множество значений функции", NodeStatus.to_learn],
             ["node27", "Основные элементарные функции", NodeStatus.to_learn],
             ["node28", "Обратная функция. График обратной функции", NodeStatus.to_learn],
             ["node29", "Линейная функция, ее график", NodeStatus.to_learn],
             ["node30", "Квадратичная функция, ее график", NodeStatus.to_learn],
             ["node31", "Степенная функция с натуральным показателем, ее график", NodeStatus.to_learn],
             ["node32", "Преобразования графиков: параллельный перенос, симметрия относительно осей координат", NodeStatus.to_learn],
             ["node33", "Тригонометрические функции, их графики", NodeStatus.to_learn],
             ["node34", "Четность и нечетность функции", NodeStatus.to_learn],
             ["node35", "Периодичность функции", NodeStatus.to_learn],
             ["node36", "Ограниченность функции", NodeStatus.to_learn],
             ["node37", "Монотонность функции. Промежутки возрастания и убывания", NodeStatus.to_learn],
             ["node38", "Точки экстремума (локального максимума и минимума) функции", NodeStatus.to_learn],
             ["node39", "Уравнения", NodeStatus.to_learn],
             ["node40", "Квадратные уравнения", NodeStatus.to_learn],
             ["node41", "Рациональные уравнения", NodeStatus.to_learn],
             ["node42", "Неравенства", NodeStatus.to_learn],
             ["node43", "Метод интервалов", NodeStatus.to_learn],
             ["node44", "Наибольшее и наименьшее значения функции", NodeStatus.to_learn],
             ["node45", "Иррациональные уравнения", NodeStatus.to_learn],
             ["node46", "Показательные уравнения", NodeStatus.to_learn],
             ["node47", "Логарифмические уравнения", NodeStatus.to_learn],
             ["node48", "Использование свойств и графиков функций при решении неравенств", NodeStatus.to_learn],
             ["node49", "Использование свойств и графиков функций при решении уравнений", NodeStatus.to_learn],
             ["node50",
              "Изображение на координатной плоскости множества решений уравнений с двумя переменными и их систем",
              NodeStatus.to_learn],
             ["node51",
              "Изображение на координатной плоскости множества решений неравенств с двумя переменными и их систем",
              NodeStatus.to_learn],
             ["node52", "Тригонометрические уравнения", NodeStatus.to_learn],
             ["node53",
              "Основные приемы решения систем уравнений: подстановка, алгебраическое сложение, введение новых переменных",
              NodeStatus.to_learn],
             ["node54", "Равносильность уравнений, систем уравнений", NodeStatus.to_learn],
             ["node55", "Простейшие системы уравнений с двумя неизвестными", NodeStatus.to_learn],
             ["node56", "Рациональные неравенства", NodeStatus.to_learn],
             ["node57", "Квадратные неравенства", NodeStatus.to_learn],
             ["node58", "Системы линейных неравенств", NodeStatus.to_learn],
             ["node59", "Системы неравенств с одной переменной", NodeStatus.to_learn],
             ["node60", "Равносильность неравенств, систем неравенств", NodeStatus.to_learn],
             ["node61", "Логарифмические неравенства", NodeStatus.to_learn],
             ["node62", "Показательные неравенства", NodeStatus.to_learn],
             ["node63", "Применение производной к исследованию функций и построению графиков", NodeStatus.to_learn],
             ["node64", "Понятие о производной функции, геометрический смысл производной", NodeStatus.to_learn],
             ["node65",
              "Физический смысл производной, нахождение скорости для процесса, заданного формулой или графиком",
              NodeStatus.to_learn],
             ["node66", "Уравнение касательной к графику функции", NodeStatus.to_learn],
             ["node67", "Первообразные элементарных функций", NodeStatus.to_learn],
             ["node68", "Производные суммы, разности, произведения, частного", NodeStatus.to_learn],
             ["node69", "Производные основных элементарных функций", NodeStatus.to_learn],
             ["node70", "Примеры применения интеграла в физике и геометрии", NodeStatus.to_learn],
             ["node71", "Вторая производная и ее физический смысл", NodeStatus.to_learn],
             ["node72", "Синус, косинус, тангенс, котангенс произвольного угла", NodeStatus.to_learn],
             ["node73", "Радианная мера угла", NodeStatus.to_learn],
             ["node74", "Основные тригонометрические тождества", NodeStatus.to_learn],
             ["node75", "Синус, косинус, тангенс и котангенс числа", NodeStatus.to_learn],
             ["node76", "Формулы приведения", NodeStatus.to_learn],
             ["node77", "Синус, косинус и тангенс суммы и разности двух углов", NodeStatus.to_learn],
             ["node78", "Синус и косинус двойного угла", NodeStatus.to_learn],
             ["node79", "Точка", NodeStatus.to_learn],
             ["node80", "Прямая", NodeStatus.to_learn],
             ["node81", "Угол", NodeStatus.to_learn],
             ["node82", "Отрезок", NodeStatus.to_learn],
             ["node83", "Аксиомы планиметрии", NodeStatus.to_learn],
             ["node84", "Измерение отрезков и углов", NodeStatus.to_learn],
             ["node85", "Треугольник", NodeStatus.to_learn],
             ["node86", "Луч", NodeStatus.to_learn],
             ["node87", "Геометрические построения - окружность", NodeStatus.to_learn],
             ["node88", "Признаки и свойства равенства треугольников", NodeStatus.to_learn],
             ["node89", "Параллельность. Сумма углов треугольника", NodeStatus.to_learn],
             ["node90", "Геометрические неравенства", NodeStatus.to_learn],
             ["node91", "Периметр и площадь треугольника", NodeStatus.to_learn],
             ["node92", "Геометрическое место точек", NodeStatus.to_learn],
             ["node93", "Касательная к окружности", NodeStatus.to_learn],
             ["node94", "Средняя линия треугольника", NodeStatus.to_learn],
             ["node95", "Трапеция", NodeStatus.to_learn],
             ["node96", "Многоугольник", NodeStatus.to_learn],
             ["node97", "Теорема Фалеса. Теорема о пропорциональных отрезках", NodeStatus.to_learn],
             ["node98", "Биссектриса, срединный перпендикуляр, медиана треугольника", NodeStatus.to_learn],
             ["node99", "Параллелограмм", NodeStatus.to_learn],
             ["node100", "Подобные треугольники", NodeStatus.to_learn],
             ["node101", "Площадь чертырёхугольника", NodeStatus.to_learn],
             ["node102", "Теорема Пифагора", NodeStatus.to_learn],
             ["node103", "Теорема Менелая и теорема Чевы", NodeStatus.to_learn],
             ["node104", "Вписанный угол", NodeStatus.to_learn],
             ["node105", "Декартовы координаты на плоскости", NodeStatus.to_learn],
             ["node106", "Пропорциональные отрезки в круге", NodeStatus.to_learn],
             ["node107", "Векторы", NodeStatus.to_learn],
             ["node108", "Теорема синусов", NodeStatus.to_learn],
             ["node109", "Теорема косинусов", NodeStatus.to_learn],
             ["node110", "Аксиомы стереометрии", NodeStatus.to_learn],
             ["node111", "Проекция, наклонная", NodeStatus.to_learn],
             ["node112", "Многогранник", NodeStatus.to_learn],
             ["node113", "Плоскость", NodeStatus.to_learn],
             ["node114", "Взаимное расположение прямых и плоскостей в стереометрии", NodeStatus.to_learn],
             ["node115", "Построение сечений в стереометрии", NodeStatus.to_learn],
             ["node116", "Параллелепипед", NodeStatus.to_learn],
             ["node117", "Теорема о трех перпендикулярах", NodeStatus.to_learn],
             ["node118", "Свойства и формулы для призмы", NodeStatus.to_learn],
             ["node119", "Призма", NodeStatus.to_learn],
             ["node120", "Тетраэдр", NodeStatus.to_learn],
             ["node121", "Пирамида", NodeStatus.to_learn],
             ["node122", "Свойства и формулы для тетраэдра", NodeStatus.to_learn],
             ["node123", "Шар", NodeStatus.to_learn],
             ["node124", "Описанные вокруг сферы сущности", NodeStatus.to_learn],
             ["node125", "Формулы для объема и площади пирамиды", NodeStatus.to_learn],
             ["node126", "Двугранный угол", NodeStatus.to_learn],
             ["node127", "Сфера", NodeStatus.to_learn],
             ["node128", "Объем и площадь боковой и полной поверхностей цилиндра", NodeStatus.to_learn],
             ["node129", "Конус", NodeStatus.to_learn],
             ["node130", "Цилиндр", NodeStatus.to_learn]],
            "edges": [
        ["node1", "node4"], ["node1", "node5"], ["node4", "node6"], ["node2", "node5"], ["node2", "node8"],
        ["node5", "node6"],
        ["node3", "node25"], ["node3", "node7"], ["node3", "node23"], ["node3", "node5"], ["node6", "node7"],
        ["node6", "node12"],
        ["node17", "node18"], ["node17", "node19"], ["node17", "node20"], ["node17", "node21"], ["node17", "node22"],
        ["node17", "node23"],
        ["node14", "node17"], ["node72", "node109"], ["node72", "node108"], ["node72", "node76"], ["node72", "node75"],
        ["node72", "node74"],
        ["node72", "node73"], ["node33", "node72"], ["node74", "node76"], ["node74", "node77"], ["node74", "node78"],
        ["node25", "node64"],
        ["node25", "node39"], ["node25", "node26"], ["node25", "node27"], ["node27", "node29"], ["node27", "node31"],
        ["node42", "node57"],
        ["node27", "node33"], ["node27", "node28"], ["node27", "node69"], ["node53", "node49"], ["node54", "node53"],
        ["node55", "node53"],
        ["node42", "node43"], ["node42", "node56"], ["node42", "node58"], ["node42", "node61"], ["node42", "node62"],
        ["node42", "node90"],
        ["node39", "node42"], ["node39", "node46"], ["node39", "node40"], ["node39", "node41"], ["node39", "node52"],
        ["node39", "node54"],
        ["node39", "node55"], ["node24", "node39"], ["node39", "node48"], ["node39", "node47"], ["node57", "node58"],
        ["node64", "node65"],
        ["node56", "node58"], ["node61", "node58"], ["node62", "node58"], ["node64", "node66"], ["node64", "node69"],
        ["node64", "node67"],
        ["node38", "node64"], ["node13", "node14"], ["node13", "node36"], ["node13", "node47"], ["node31", "node13"],
        ["node12", "node13"],
        ["node33", "node18"], ["node33", "node35"], ["node33", "node34"], ["node33", "node37"], ["node33", "node108"],
        ["node33", "node109"],
        ["node33", "node52"], ["node81", "node33"], ["node33", "node81"], ["node71", "node63"], ["node68", "node71"],
        ["node69", "node71"],
        ["node44", "node48"], ["node60", "node48"], ["node63", "node48"], ["node48", "node51"], ["node28", "node29"],
        ["node28", "node31"],
        ["node28", "node32"], ["node28", "node37"], ["node26", "node28"], ["node37", "node38"], ["node26", "node38"],
        ["node36", "node38"],
        ["node38", "node44"], ["node11", "node12"], ["node31", "node12"], ["node12", "node47"], ["node44", "node49"],
        ["node63", "node49"],
        ["node49", "node50"], ["node78", "node52"], ["node77", "node78"], ["node14", "node15"], ["node14", "node16"],
        ["node7", "node11"],
        ["node8", "node7"], ["node30", "node37"], ["node29", "node30"], ["node34", "node35"], ["node37", "node34"],
        ["node34", "node36"],
        ["node76", "node77"], ["node23", "node24"], ["node59", "node60"], ["node58", "node59"], ["node47", "node46"],
        ["node41", "node45"],
        ["node65", "node68"], ["node67", "node65"], ["node67", "node70"], ["node66", "node68"], ["node127", "node124"],
        ["node129", "node124"],
        ["node119", "node124"], ["node116", "node124"], ["node120", "node124"], ["node121", "node124"],
        ["node121", "node130"],
        ["node121", "node127"], ["node121", "node125"], ["node121", "node129"], ["node116", "node121"],
        ["node123", "node121"],
        ["node120", "node121"], ["node112", "node121"], ["node121", "node119"], ["node119", "node118"],
        ["node119", "node116"], ["node120", "node119"], ["node112", "node119"], ["node112", "node113"],
        ["node112", "node110"], ["node112", "node116"], ["node113", "node112"], ["node110", "node112"],
        ["node112", "node120"],
        ["node113", "node114"], ["node113", "node117"], ["node113", "node115"], ["node113", "node126"],
        ["node126", "node113"], ["node127", "node123"], ["node127", "node129"], ["node127", "node130"],
        ["node126", "node127"], ["node116", "node117"], ["node114", "node117"], ["node111", "node117"],
        ["node83", "node110"],
        ["node115", "node110"], ["node110", "node111"], ["node111", "node114"],
        ["node120", "node122"], ["node130", "node128"], ["node99", "node116"],
        ["node79", "node80"], ["node80", "node79"], ["node87", "node92"], ["node87", "node93"], ["node87", "node97"],
        ["node87", "node109"],
        ["node80", "node87"], ["node85", "node89"], ["node85", "node98"], ["node85", "node92"], ["node85", "node94"],
        ["node101", "node85"], ["node85", "node102"], ["node85", "node91"], ["node85", "node83"], ["node85", "node82"],
        ["node82", "node85"],
        ["node97", "node106"], ["node97", "node105"], ["node97", "node107"], ["node97", "node102"],
        ["node97", "node100"], ["node97", "node103"],
        ["node97", "node108"], ["node95", "node97"], ["node84", "node97"], ["node97", "node101"], ["node89", "node97"],
        ["node82", "node84"],
        ["node82", "node81"], ["node81", "node82"], ["node81", "node84"], ["node81", "node80"], ["node80", "node81"],
        ["node79", "node87"],
        ["node98", "node101"], ["node96", "node101"],
        ["node101", "node99"], ["node101", "node108"], ["node107", "node101"], ["node101", "node109"],
        ["node101", "node95"], ["node102", "node101"], ["node105", "node101"],
        ["node108", "node109"], ["node104", "node108"], ["node100", "node108"],
        ["node99", "node108"], ["node109", "node108"], ["node102", "node108"],
        ["node86", "node89"], ["node86", "node83"], ["node83", "node86"], ["node99", "node109"], ["node91", "node109"],
        ["node102", "node109"], ["node98", "node100"], ["node94", "node100"], ["node89", "node100"],
        ["node100", "node104"], ["node88", "node94"],
        ["node98", "node94"], ["node94", "node91"], ["node94", "node95"], ["node88", "node89"],
        ["node84", "node89"], ["node89", "node96"], ["node89", "node90"], ["node107", "node99"],
        ["node91", "node99"], ["node96", "node99"], ["node98", "node99"],
        ["node90", "node96"], ["node96", "node95"], ["node92", "node98"], ["node92", "node91"], ["node80", "node93"],
        ["node93", "node104"],
        ["node104", "node106"], ["node103", "node106"], ["node105", "node107"], ["node102", "node105"],
        ["node84", "node88"]]
    }


id_to_index_math = {row[0]: index for index, row in enumerate(math_graph["nodes"])}