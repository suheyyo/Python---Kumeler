#python koleksiyonlar (diziler) altında yer alan küme (set) veri tipi, sıralanamayan, değiştirilemeyen, indexlenemeyen ve çoğul elemana izin verilmeyen bir veri tipidir. {} parantezleriyle oluşturulur. eleman olmadan sadece pparantezlerle boş bir küme oluşturulamaz.
#set() fonksiyonu ile de oluşturulabilir. constructor yöntemiyle başlangıçta elemanları ayarlanabilir.
kume = set()
kume = set(("ankara", "istanbul", "kayseri"))
#indeks olmadığı için döngüyle elemanları yazdırılabilir.
kume = {"elma", "armut", "çilek"}
for x in kume:
    print(x)
#eleman sayısı için len()
kume = {"elma", "armut", "çilek"}
print(len(kume))
#elemanın olup olmadığını kontrol etme
kume = {"elma", "armut", "çilek"}
print ("elma" in kume) #True
print ("ananas" in kume) #False
#elemanlar demetlerdeki gibi değiştirilemez.
#kümeye yeni bir eleman eklemek için add() fonksiyonu kullanılabilir.
kume = {"elma", "armut", "çilek"}
kume.add("ananas")
print(kume) #{"elma", "ananas", "armut", "çilek"} 
#indeks numarası olmadığı için rastgele yazılmış bir şekilde çıktısı olabilir.
#birden fazla eleman eklenmek isteniyorsa update()
kume = {"elma", "armut", "çilek"}
kume.update(["ananas", "kivi", "portakal"])
print(kume) #{"elma", "kivi", "ananas", "armut", "çilek", "portakal"}
#kümeye liste ve demet de ekleyebiliriz. (update() yoluyla)
kume = {"elma", "armut", "çilek"}
liste = ["x", "y", "z"]
demet = (1,2,3)
kume.update(liste)
kume.update(demet)
print(kume) 
#discard ve remove
kume = {"elma", "armut", "çilek"}
kume.remove("elma")
print(kume)
kume = {"elma", "armut", "çilek"}
kume.discard("elma")
print(kume)
#olmayan bir elemanı discard ile çıkarırsak hata vermez. ama remove verir. aralarındaki fark budur.
#kümenin son elemanını çıkarmak için pop() kullanırız. ama indexlenme olmadığı için rastgele bir eleman çıkabilir.
kume = {"elma", "armut", "çilek"}
kume.pop()
print(kume)
#kümeyi boşaltmak istediğinde clear() kullanılır.
kume = {"elma", "armut", "çilek"}
kume.clear()
print(kume) #set()
#kümeyi tamamen silmek del kullanılır. kümeyi sildikten sonra çalıştırırsan hata alırsın.
kume = {"elma", "armut", "çilek"}
del kume
print(kume) #!!HATA VERİR!!
#küme kopyalamak ve çoğaltmak
kume = {"elma", "armut", "çilek"}
yenikume = kume.copy()
print(yenikume) #{"elma", "armut", "çilek"}
#başka bir yöntem de kopyalanacak kümeyi belirterek yeni bir küme oluşturmaktır.
kume = {"elma", "armut", "çilek"}
yenikume = set(kume)
print(yenikume) #{"elma", "armut", "çilek"}
#birbirinden farklı veya aynı kümeyi birleştirmek için union() veya update kullanılabilir.
kume1 = {"a", "b", "c"}
kume2 = {"d", "e"}
kume3 = kume1.union(kume2)
print(kume3)    #{"c", "b", "d", "a", "e"}
kume1 = {"a", "b", "c"}
kume2 = {"d", "e"}
kume3 = kume1.update(kume2)
print(kume3)    #{"c", "b", "d", "a", "e"}
#küme birleştirilirken aynı elemandan birkaç tane varsa o elemanı tek defa yazdıracaktır.
kume1 = {"a", "b", "c"}
kume2 = {"a", "d", "e"}
kume3 = kume1.union(kume2)
print(kume3)    #{"c", "b", "d", "a", "e"}
#mevcut iki kümenin kesişimi olup olmadığını öğrenmek için isdisjoint() fonksiyonu kullanılır, eğer varsa FALSE, yoksa TRUE çıktısı alınır.
kume1 = {"a", "b", "c"}
kume2 = {"a", "d"}
kume3 = {"f", "g"}
print(kume1.isdisjoint(kume2)) #False
print(kume1.isdisjoint(kume3)) #True
#iki farklı kümenin kesişimini almak için intersection() fonksiyonu kullanılabilir.
kume1 = {"a", "b", "c"}
kume2 = {"a", "d"}
kesisim = kume1.intersection(kume2)
print(kesisim)  #{"a"}
#eğer ikği kümenin kesişimi alındıktan sonra küme bu kesişim elemanlarıyla güncellenmek istenirse intersection_update() fonksiyonu kullanılabilir.
kume1 = {"a", "b", "c"}
kume2 = {"a", "d"}
kesisim = kume1.intersection_update(kume2)
print(kume1)  #{"a"}
#bir kümenin diğer kümeden farkını almak için difference() kullanılır.
kume1 = {"a", "b", "c"}
kume2 = {"a", "d", "c", "b"}
fark = kume1.difference(kume2)
print(fark) #{"d"}
#update difference
kume1 = {"a", "b", "c"}
kume2 = {"a", "d", "c", "b"}
fark = kume1.difference_update(kume2)
print(kume1)  #{"d"}
#kümenin alt kümeye sahip olup olmadığını kontrol etme issubset()kullanılır.
kume1 = {"a", "b"}
kume2 = {"a", "b", "c", "d"}
print(kume1.issubset(kume2))
#issuperset üst küme
kume1 = {"a", "b"}
kume2 = {"a", "b", "c", "d"}
print(kume2.issuperset(kume1))  #True
#for döngüsü ile kullanıcıdan 10 tane sayı isteyerek bir küme oluşturun. for döngüsü ile kullanıcıdan 10 tane sayı isteyerek farklı bir küme oluşturun. her iki kümenin kesişimi olup olmadığını ekrana yazdırın. her iki kümenin kesişimi ile yeni bir küme oluşturun ve ekrana yazdırın. kullanıcıya 3 kümeyi de ayrı ayrı olarak silmek isteyip istemediğini sorunun verdiği cevaba göre ilgili işlemi yapınız.
kume1 = set()
print("Birinci küme için 10 sayı girin:")
for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    kume1.add(sayi)
kume2 = set()
print("\nİkinci küme için 10 sayı girin:")
for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    kume2.add(sayi)
kesisim = kume1 & kume2
if kesisim:
    print(f"\nHer iki kümenin kesişimi vardır: {kesisim}")
else:
    print("\nHer iki kümenin kesişimi yoktur.")
kesisim_kume = kesisim
print(f"\nKümelerin kesişimi ile oluşturulan yeni küme: {kesisim_kume}")
def kume_sil(kume_adı, kume):
    cevap = input(f"{kume_adı} kümesini silmek ister misiniz? (Evet/Hayır): ").strip().lower()
    if cevap == "evet":
        kume.clear()
        print(f"{kume_adı} kümesi silindi.")
    else:
        print(f"{kume_adı} kümesi silinmedi.")
kume_sil("Birinci", kume1)
kume_sil("İkinci", kume2)
kume_sil("Kesişim", kesisim_kume)
print(f"\nBirinci küme: {kume1}")
print(f"İkinci küme: {kume2}")
print(f"Kesişim kümesi: {kesisim_kume}")

kume = set()
while True:
    x = input("isim giriniz (çıkmak için 'exit' yazın): ")
    if x.lower() == "exit":
        break
    kume.add(x)
print("küme içeriği:", kume)
print("kümedeki eleman sayısı:", len(kume))
