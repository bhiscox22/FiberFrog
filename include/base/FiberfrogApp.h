#ifndef FIBERFROGAPP_H
#define FIBERFROGAPP_H

#include "MooseApp.h"

class FiberfrogApp;

template<>
InputParameters validParams<FiberfrogApp>();

class FiberfrogApp : public MooseApp
{
public:
  FiberfrogApp(InputParameters parameters);
  virtual ~FiberfrogApp();

  static void registerApps();
  static void registerObjects(Factory & factory);
  static void associateSyntax(Syntax & syntax, ActionFactory & action_factory);
};

#endif /* FIBERFROGAPP_H */
