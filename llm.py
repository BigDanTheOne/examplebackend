from openai import OpenAI
import httpx
API_KEY = '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'
proxies = {
   'http://': 'http://20.163.133.5:80',
   'https://': 'https://20.206.106.192:80',
}

client = OpenAI(api_key=API_KEY)

subject = "математика"
def make_prompt(subject):
  return "Изучи код для библиотеки graph.js для построения максимально подробного и покрывающего тему графа знаний для полного изучения школьной математики. тебе надо предоставить такого же вида код, который строит максимально подробный ориентированный граф для максимального изучения темы" + subject + ". Для этого возьми все вершины и взаимосвязи из прикрепленного мною кода по математике и постарайся от них прийти к новым вершинам по теме " + subject + " - это важно. " \
  "потому что частично твоя новая тема строится на школьной математике (если всё-таки какие-то вершины даже максимально отдалённо связаны значит веди от них и декомпозируй сильнее остальные темы), оставь нужное для темы " + subject + " и предоставь мне новый код. используй по возможности и прописывай явно при декомпозиции (а нужна очень глубокая) связанных вершин в графе взаимосвязи, которые ты видел или " \
  "создавал в этом диалоге. и в будущем используй и связывай между собой.:" \
  """result = {
      "nodes": [
          ["id", "title", status],
          ["node1", "Целые числа", status],
          ["node2", "Натуральные числа", status],
          ["node3", "Действительные числа", status],
          ["node4", "Степень с целым показателем", status],
          ["node5", "Дроби, проценты, рациональные числа", status],
          ["node6", "Степень с рациональным показателем и ее свойства", status],
          ["node7", "Свойства степени с действительным показателем", status],
          ["node8", "Степень с натуральным показателем", status],
          ["node9", "Свойства степени с действительным показателем", status],
          ["node11", "Корень степени и его свойства, status],
          ["node12", "Показательная функция, ее график", status],
          ["node13", "Логарифмическая функция, ее график", status],
          ["node14", "Логарифм числа", status],
          ["node15", "Логарифм произведения, частного, степени", status],
          ["node16", "Десятичный и натуральный логарифмы, число е", status],
          ["node17", "Преобразования выражений", status],
          ["node18", "Преобразования тригонометрических выражений", status],
          ["node19", "Преобразования выражений, включающих арифметические операции", status],
          ["node20", "Преобразования выражений, включающих корни натуральной степени", status],
          ["node21", "Преобразования выражений, включающих операцию возведения в степень", status],
          ["node22", "Преобразование выражений, включающих операцию логарифмирования", status],
          ["node23", "Модуль (абсолютная величина) числа", status],
          ["node24", "Свойства модуля", status],
          ["node25", "Функция, область определения функции", status],
          ["node26", "Множество значений функции", status],
          ["node27", "Основные элементарные функции", status],
          ["node28", "Обратная функция. График обратной функции", status],
          ["node29", "Линейная функция, ее график", status],
          ["node30", "Квадратичная функция, ее график", status],
          ["node31", "Степенная функция с натуральным показателем, ее график", status],
          ["node32", "Преобразования графиков: параллельный перенос, симметрия относительно осей координат", status],
          ["node33", "Тригонометрические функции, их графики", status],
          ["node34", "Четность и нечетность функции", status],
          ["node35", "Периодичность функции", status],
          ["node36", "Ограниченность функции", status],
          ["node37", "Монотонность функции. Промежутки возрастания и убывания", status],
          ["node38", "Точки экстремума (локального максимума и минимума) функции", status],
          ["node39", "Уравнения", status],
          ["node40", "Квадратные уравнения", status],
          ["node41", "Рациональные уравнения", status],
          ["node42", "Неравенства", status],
          ["node43", "Метод интервалов", status],
          ["node44", "Наибольшее и наименьшее значения функции", status],
          ["node45", "Иррациональные уравнения", status],
          ["node46", "Показательные уравнения", status],
          ["node47", "Логарифмические уравнения", status],
          ["node48", "Использование свойств и графиков функций при решении неравенств", status],
          ["node49", "Использование свойств и графиков функций при решении уравнений", status],
          ["node50", "Изображение на координатной плоскости множества решений уравнений с двумя переменными и их систем", status],
          ["node51", "Изображение на координатной плоскости множества решений неравенств с двумя переменными и их систем", status],
          ["node52", "Тригонометрические уравнения", status],
          ["node53", "Основные приемы решения систем уравнений: подстановка, алгебраическое сложение, введение новых переменных", status],
          ["node54", "Равносильность уравнений, систем уравнений", status],
          ["node55", "Простейшие системы уравнений с двумя неизвестными", status],
          ["node56", "Рациональные неравенства", status],
          ["node57", "Квадратные неравенства", status],
          ["node58", "Системы линейных неравенств", status],
          ["node59", "Системы неравенств с одной переменной", status],
          ["node60", "Равносильность неравенств, систем неравенств", status],
          ["node61", "Логарифмические неравенства", status],
          ["node62", "Показательные неравенства", status],
          ["node63", "Применение производной к исследованию функций и построению графиков", status],
          ["node64", "Понятие о производной функции, геометрический смысл производной", status],
          ["node65", "Физический смысл производной, нахождение скорости для процесса, заданного формулой или графиком", status],
          ["node66", "Уравнение касательной к графику функции", status],
          ["node67", "Первообразные элементарных функций", status],
          ["node68", "Производные суммы, разности, произведения, частного", status],
          ["node69", "Производные основных элементарных функций", status],
          ["node70", "Примеры применения интеграла в физике и геометрии", status],
          ["node71", "Вторая производная и ее физический смысл", status],
          ["node72", "Синус, косинус, тангенс, котангенс произвольного угла", status],
          ["node73", "Радианная мера угла", status],
          ["node74", "Основные тригонометрические тождества", status],
          ["node75", "Синус, косинус, тангенс и котангенс числа", status],
          ["node76", "Формулы приведения", status],
          ["node77", "Синус, косинус и тангенс суммы и разности двух углов", status],
          ["node78", "Синус и косинус двойного угла", status],
          ["node79", "Точка", status],
          ["node80", "Прямая", status],
          ["node81", "Угол", status],
          ["node82", "Отрезок", status],
          ["node83", "Аксиомы планиметрии", status],
          ["node84", "Измерение отрезков и углов", status],
          ["node85", "Треугольник", status],
          ["node86", "Луч", status],
          ["node87", "Геометрические построения - окружность", status],
          ["node88", "Признаки и свойства равенства треугольников", status],
          ["node89", "Параллельность. Сумма углов треугольника", status],
          ["node90", "Геометрические неравенства", status],
          ["node91", "Периметр и площадь треугольника", status],
          ["node92", "Геометрическое место точек", status],
          ["node93", "Касательная к окружности", status],
          ["node94", "Средняя линия треугольника", status],
          ["node95", "Трапеция", status],
          ["node96", "Многоугольник", status],
          ["node97", "Теорема Фалеса. Теорема о пропорциональных отрезках", status],
          ["node98", "Биссектриса, срединный перпендикуляр, медиана треугольника", status],
          ["node99", "Параллелограмм", status],
          ["node100", "Подобные треугольники", status],
          ["node101", "Площадь чертырёхугольника", status],
          ["node102", "Теорема Пифагора", status],
          ["node103", "Теорема Менелая и теорема Чевы", status],
          ["node104", "Вписанный угол", status],
          ["node105", "Декартовы координаты на плоскости", status],
          ["node106", "Пропорциональные отрезки в круге", status],
          ["node107", "Векторы", status],
          ["node108", "Теорема синусов", status],
          ["node109", "Теорема косинусов", status],
          ["node110", "Аксиомы стереометрии", status],
          ["node111", "Проекция, наклонная", status],
          ["node112", "Многогранник", status],
          ["node113", "Плоскость", status],
          ["node114", "Взаимное расположение прямых и плоскостей в стереометрии", status],
          ["node115", "Построение сечений в стереометрии", status],
          ["node116", "Параллелепипед", status],
          ["node117", "Теорема о трех перпендикулярах", status],
          ["node118", "Свойства и формулы для призмы", status],
          ["node119", "Призма", status],
          ["node120", "Тетраэдр", status],
          ["node121", "Пирамида", status],
          ["node122", "Свойства и формулы для тетраэдра", status],
          ["node123", "Шар", status],
          ["node124", "Описанные вокруг сферы сущности", status],
          ["node125", "Формулы для объема и площади пирамиды", status],
          ["node126", "Двугранный угол", status],
          ["node127", "Сфера", status],
          ["node128", "Объем и площадь боковой и полной поверхностей цилиндра", status],
          ["node129", "Конус", status],
          ["node130", "Цилиндр", status],
  
      ],
      "edges": [
          ["node1", "node4"],["node1", "node5"],["node4", "node6"],["node2", "node5"],["node2", "node8"],["node5", "node6"],
          ["node3", "node25"],["node3", "node7"],["node3", "node23"],["node3", "node5"],["node6", "node7"],["node6", "node12"],
          ["node17", "node18"],["node17", "node19"],["node17", "node20"],["node17", "node21"],["node17", "node22"],["node17", "node23"],
          ["node14", "node17"],["node72", "node109"],["node72", "node108"],["node72", "node76"],["node72", "node75"],["node72", "node74"],
          ["node72", "node73"],["node33", "node72"],["node74", "node76"],["node74", "node77"],["node74", "node78"],["node25", "node64"],
          ["node25", "node39"],["node25", "node26"],["node25", "node27"],["node27", "node29"],["node27", "node31"],["node42", "node57"],
          ["node27", "node33"],["node27", "node28"],["node27", "node69"],["node53", "node49"],["node54", "node53"],["node55", "node53"],
          ["node42", "node43"],["node42", "node56"],["node42", "node58"],["node42", "node61"],["node42", "node62"],["node42", "node90"],	
          ["node39", "node42"],["node39", "node46"],["node39", "node40"],["node39", "node41"],["node39", "node52"],["node39", "node54"],
          ["node39", "node55"],["node24", "node39"],["node39", "node48"],["node39", "node47"],["node57", "node58"],["node64", "node65"],
          ["node56", "node58"],["node61", "node58"],["node62", "node58"],["node64", "node66"],["node64", "node69"],["node64", "node67"],
          ["node38", "node64"],["node13", "node14"],["node13", "node36"],["node13", "node47"],["node31", "node13"],["node12", "node13"],
          ["node33", "node18"],["node33", "node35"],["node33", "node34"],["node33", "node37"],["node33", "node108"],["node33", "node109"],
          ["node33", "node52"],["node81", "node33"],["node33", "node81"],["node71", "node63"],["node68", "node71"],["node69", "node71"],
          ["node44", "node48"],["node60", "node48"],["node63", "node48"],["node48", "node51"],["node28", "node29"],["node28", "node31"],
          ["node28", "node32"],["node28", "node37"],["node26", "node28"],["node37", "node38"],["node26", "node38"],["node36", "node38"],
          ["node38", "node44"],["node11", "node12"],["node31", "node12"],["node12", "node47"],["node44", "node49"],["node63", "node49"],
          ["node49", "node50"],["node78", "node52"],["node77", "node78"],["node14", "node15"],["node14", "node16"],["node7", "node11"],
          ["node8", "node7"],["node30", "node37"],["node29", "node30"],["node34", "node35"],["node37", "node34"],["node34", "node36"],
          ["node76", "node77"],["node23", "node24"],["node59", "node60"],["node58", "node59"],["node47", "node46"],["node41", "node45"],
          ["node65", "node68"],["node67", "node65"],["node67", "node70"],["node66", "node68"],["node127", "node124"],["node129", "node124"],
          ["node119", "node124"],["node116", "node124"],["node120", "node124"],["node121", "node124"],["node121", "node130"],
          ["node121", "node127"],["node121", "node125"],["node121", "node129"],["node116", "node121"],["node123", "node121"],
          ["node120", "node121"],["node112", "node121"],["node121", "node119"],["node119", "node118"],
          ["node119", "node116"],["node120", "node119"],["node112", "node119"],["node112", "node113"],
          ["node112", "node110"],["node112", "node116"],["node113", "node112"],["node110", "node112"],["node112", "node120"],
          ["node113", "node114"],["node113", "node117"],["node113", "node115"],["node113", "node126"],
          ["node126", "node113"],["node127", "node123"],["node127", "node129"],["node127", "node130"],["node126", "node127"],["node116", "node117"],["node114", "node117"],["node111", "node117"],["node83", "node110"],
          ["node115", "node110"],	["node110", "node111"],["node111", "node114"],
          ["node120", "node122"],["node130", "node128"],["node99", "node116"],
          ["node79", "node80"],["node80", "node79"],["node87", "node92"],["node87", "node93"],["node87", "node97"],["node87", "node109"],
          ["node80", "node87"],["node85", "node89"],["node85", "node98"],["node85", "node92"],["node85", "node94"],
          ["node101", "node85"],["node85", "node102"],["node85", "node91"],["node85", "node83"],["node85", "node82"],["node82", "node85"],
          ["node97", "node106"],["node97", "node105"],["node97", "node107"],["node97", "node102"],["node97", "node100"],["node97", "node103"],
          ["node97", "node108"],["node95", "node97"],["node84", "node97"],["node97", "node101"],["node89", "node97"],["node82", "node84"],
          ["node82", "node81"],["node81", "node82"],["node81", "node84"],["node81", "node80"],["node80", "node81"],["node79", "node87"],
          ["node98", "node101"],["node96", "node101"],
          ["node101", "node99"],["node101", "node108"],["node107", "node101"],["node101", "node109"],
          ["node101", "node95"],["node102", "node101"],["node105", "node101"],
          ["node108", "node109"],["node104", "node108"],["node100", "node108"],
          ["node99", "node108"],["node109", "node108"],["node102", "node108"],
          ["node86", "node89"],["node86", "node83"],["node83", "node86"],["node99", "node109"],["node91", "node109"],["node102", "node109"],["node98", "node100"],["node94", "node100"],["node89", "node100"],["node100", "node104"],["node88", "node94"],
          ["node98", "node94"],["node94", "node91"],["node94", "node95"],["node88", "node89"],
          ["node84", "node89"],["node89", "node96"],["node89", "node90"],["node107", "node99"],
          ["node91", "node99"],["node96", "node99"],["node98", "node99"],
          ["node90", "node96"],["node96", "node95"],["node92", "node98"],["node92", "node91"],["node80", "node93"],["node93", "node104"],
  ["node104", "node106"],["node103", "node106"],["node105", "node107"],["node102", "node105"],["node84", "node88"],
      ]}"""


def build_graph(subject):
  global prompt
  response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
                 {"role": "system", "content": make_prompt('мера Лебега')},
                 {"role": "user", "content": "content"},
               ],
    temperature = 0,
    max_tokens = 1024
  )
  print(response)
  return response

build_graph('Мера Лебега')

# def text_to_summary(content):
#
#   with open('utiles/promt.txt') as f:
#       promt = "".join(f.readlines())
#   response = client.chat.completions.create(
#
#   return response.choices[0].message.content
#
#
# def text_to_summary_in_parts(content):
#   client = OpenAI(api_key=API_KEY)
#
#
#   response = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     messages=[
#       {"role": "system", "content": promt},
#       {"role": "user", "content": content},
#     ],
#     temperature=0,
#     stream=True
#   )
#   return response
#
#
# def ask_question_gpt(chat_history):
#   client = OpenAI(api_key=API_KEY)
#
#
#   response = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     messages=chat_history,
#     temperature=0,
#     stream=True
#   )
#   return response
