package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
  
  private int counters = 0;
  
  @Override
  public void insertQuarter() {
  counters++;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    switch (name) {
      case "ScottCola":
        if (counters >= 3) {
          counters -= 3;
          return new Drink() {
            @Override
            public String getName() {
              return "ScottCola";
              }
            @Override
            public boolean isFizzy() {
                return true;
            }
            };
        } else {
        throw new NotEnoughMoneyException();
        }
      case "KarenTea":
        if (counters >= 4) {
          counters -= 4;
          return new Drink() {
            @Override
            public String getName() {
              return "KarenTea";
            }
            @Override
            public boolean isFizzy() {
                return false;
            }
          };
        } else {
            throw new NotEnoughMoneyException();
          }
      default:
        throw new UnknownDrinkException();
    }
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }
}