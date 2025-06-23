import argparse
import json
def main():
    path = "/home/mert/workspace/github.com/mertsariyarr/todo_app/tasks.json"
    tasks = read_tasks(path) #Oluşturduğumuz tasks.json dosyasının içini okur, veri varsa o veriyi list olarak döner yoksa [] döner.

    parser = argparse.ArgumentParser() #cli'dan veri okumak için bir parser object oluşturduk

    parser.add_argument("--add") #cli'dan veri okumak için bir flag ekledik (--add eklemek için kullanılan flag olacak)
    
    parser.add_argument("--list", action="store_true") #cli'a list flag'ı ekledik jsondan veriyi listeleyeceğiz.
    
    parser.add_argument("--remove")

    parser.add_argument("--clear", action="store_true")

    parser.add_argument("--complete")

    args = parser.parse_args() #cli'dan yazdığımız veriyi string olarak dönecek
    
                    
    if args.add: #cli'a düzgün bir veri yazıldıysa
        tasks.append({"task": args.add, "completed": False}) #json'daki list'eye cli'dan yazdığımız veriyi ekleyecek
        with open(path, "w") as w: # güncellediğimiz listeyi json.dump() sayesinde json dosyasına yeniden yazacak
            json.dump(tasks, w)
        print(f"Görev eklendi: {args.add}")
    elif args.list: 
        for i, item in enumerate(tasks, 1):
            print(f"{i}. {item['task']}")
    elif args.remove:
        try:
            myIndex = int(args.remove) - 1
            if myIndex < 0 or myIndex >= len(tasks):
                raise IndexError
        except ValueError:
            raise Exception("Lütfen geçerli bir sayı giriniz.")
        except IndexError:
            raise Exception("Bu sıraya karşılık gelen bir görev bulunamadı.")
        
        deleted_task = tasks[myIndex]
        del tasks[myIndex]
        with open(path, "w") as w:
            json.dump(tasks, w)
        print(f"Görev başarıyla silindi: {deleted_task['task']}")
    
    elif args.clear:
        tasks.clear()
        with open(path, "w") as w:
            json.dump(tasks, w)
        print("Görev listesi başarıyla temizlendi.")
    
    elif args.complete:
        try:
            myIndex = int(args.complete) - 1
            if myIndex < 0 or myIndex >= len(tasks):
                raise IndexError
        except ValueError:
            raise Exception("Lütfen geçerli bir sayı giriniz.")
        except IndexError:
            raise Exception("Bu sıraya karşılık gelen bir görev bulunmadı")

        tasks[myIndex]["completed"] = True
        with open(path, "w") as w:
            json.dump(tasks, w)
        print(f"Görev: {tasks[myIndex]['task']} ... Tamamlandı.")
        

    else:
        print("Hiçbir görev eklenemedi.")
    
        

        


def read_tasks(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return []

main()